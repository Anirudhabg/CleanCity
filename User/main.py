import base64
import flet as ft
import json
import os
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import csv
import warnings

warnings.filterwarnings("ignore")

# Paths to files
complaints_file_path = (
    "C:/Users/LENOVO/Documents/GitHub/CleanCity/Complaints/complaints.json"
)
model_path = "model_unquant.tflite"
labels_file_path = "labels.txt"
disposal_methods_file_path = "waste.csv"


# Function to safely load complaints from file
def load_complaints():
    if os.path.exists(complaints_file_path):
        with open(complaints_file_path, "r") as file:
            try:
                return json.load(file)  # Attempt to load JSON data
            except json.JSONDecodeError:
                return []  # If the file is empty or invalid, return an empty list
    else:
        return []


# Load complaints
complaints = load_complaints()


# Function to load disposal methods from CSV file
def load_disposal_methods(file_path):
    disposal_methods = {}
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                disposal_methods[row["Waste Type"]] = row["Description"]
    except Exception as e:
        print(f"Error loading disposal methods: {e}")
    return disposal_methods


# Initialize TensorFlow model
try:
    model = tf.lite.Interpreter(model_path=model_path)
    model.allocate_tensors()
except Exception as e:
    print(f"Error loading model: {e}")

input_index = model.get_input_details()[0]["index"]
output_index = model.get_output_details()[0]["index"]

# Load labels
try:
    with open(labels_file_path, "r") as f:
        labels = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print("Error: labels.txt file not found.")

# Load disposal methods
disposal_methods = load_disposal_methods(disposal_methods_file_path)


def main(page: ft.Page):
    page.title = "CleanCity - User Application"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Regular.ttf",
    }
    page.theme = ft.Theme(font_family="Kanit")

    # Function to submit complaint
    def send_complaint(e):
        # Check if all required fields are filled
        if (
            not user_name.value
            or not user_phone.value
            or not complaint_text.value
            or not location.value
        ):
            page.snack_bar = ft.SnackBar(ft.Text("Please fill out all fields."))
            page.snack_bar.open = True
            page.update()
            return  # Exit the function if validation fails

        new_complaint = {
            "user": user_name.value,
            "phone_number": user_phone.value,
            "email": user_email.value,
            "complaint": complaint_text.value,
            "location": location.value,
            "status": "Pending",
        }
        complaints.append(new_complaint)

        # Store the complaints in the file to simulate persistence
        with open(complaints_file_path, "w") as file:
            json.dump(complaints, file)

        user_name.value = ""
        complaint_text.value = ""
        location.value = ""
        page.snack_bar = ft.SnackBar(ft.Text("Complaint sent successfully!"))
        page.snack_bar.open = True
        page.update()

    # Function to classify image
    def classify_image(e):
        try:
            if e.files:
                file_path = e.files[0].path

                # Process and classify image
                image = Image.open(file_path)
                image = image.resize((224, 224))
                image_array = (
                    np.array(image).reshape((1, 224, 224, 3)).astype(np.float32)
                )
                image_array = image_array / 255.0

                model.set_tensor(input_index, image_array)
                model.invoke()
                output = model.get_tensor(output_index)

                predicted_index = np.argmax(output)
                predicted_class = labels[predicted_index]

                result_text.value = f"Predicted class: {predicted_class}"

                # Display corresponding disposal method
                pred = predicted_class[
                    2::
                ]  # Adjust the index slicing based on your labels' format
                disposal_text.value = (
                    f"Disposal Method: {disposal_methods.get(pred, 'Not found')}"
                )

                # Display the uploaded image
                image_control.src_base64 = base64.b64encode(
                    open(file_path, "rb").read()
                ).decode("utf-8")

                page.update()

        except Exception as ex:
            print(f"Error in classification: {ex}")
            result_text.value = "Error in processing the image."
            page.update()

    # User interface elements for complaint submission
    user_name = ft.TextField(label="Your Name", width=300)
    user_phone = ft.TextField(
        label="Phone Number", width=300, keyboard_type=ft.KeyboardType.NUMBER
    )
    user_email = ft.TextField(
        label="Email", width=300, keyboard_type=ft.KeyboardType.EMAIL
    )
    complaint_text = ft.TextField(
        label="Complaint about trash", multiline=True, width=300
    )
    location = ft.TextField(
        label="Location", multiline=True, width=300, height=100
    )  # Manual location input
    send_button = ft.ElevatedButton(text="Send Complaint", on_click=send_complaint)

    # User interface elements for image classification
    image_control = ft.Image(width=224, height=224)
    result_text = ft.Text()
    disposal_text = ft.Text()

    file_picker = ft.FilePicker(on_result=classify_image)
    page.overlay.append(file_picker)
    instruction_text = ft.Text(
        "Submit an image to get proper disposal method.", size=24
    )

    # Layout for the user complaint form
    complaint_form = ft.Column(
        [
            ft.Text(
                "CleanCity - User Application",
                size=34,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Text("Submit a Complaint", size=20),
            user_name,
            user_phone,
            user_email,
            complaint_text,
            location,
            send_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    # Layout for the image classification section
    classification_section = ft.Column(
        [
            instruction_text,
            ft.ElevatedButton(
                "Select Image", on_click=lambda _: file_picker.pick_files()
            ),
            image_control,
            result_text,
            disposal_text,
        ],
        scroll=ft.ScrollMode.ADAPTIVE,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    colm = ft.Column(
        [complaint_form, classification_section],
        scroll=ft.ScrollMode.ALWAYS,
    )

    # Add both sections to the page
    page.add(
        ft.Container(
            content=colm,
            width=375,
            height=667,
            border=ft.border.all(2, ft.colors.WHITE),
            padding=10,
            border_radius=ft.border_radius.all(5),
            alignment=ft.alignment.center,
        ),
    )


ft.app(target=main)
