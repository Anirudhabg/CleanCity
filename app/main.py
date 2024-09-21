import base64
import flet as ft
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import csv
import warnings

warnings.filterwarnings('ignore')

def load_disposal_methods(file_path):
    disposal_methods = {}
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            disposal_methods[row['Waste Type']] = row['Description']
    return disposal_methods

def main(page: ft.Page):
    page.title = "Waste Garbage Classification"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 50

    model = tf.lite.Interpreter(model_path="model_unquant.tflite")
    model.allocate_tensors()

    input_index = model.get_input_details()[0]["index"]
    output_index = model.get_output_details()[0]["index"]

    with open("labels.txt", "r") as f:
        labels = [line.strip() for line in f.readlines()]

    disposal_methods = load_disposal_methods("waste.csv")

    image_control = ft.Image(width=224, height=224)
    result_text = ft.Text()
    disposal_text = ft.Text()

    def classify_image(e):
        if e.files:
            file_path = e.files[0].path
            
            image = Image.open(file_path)
            image = image.resize((224, 224))
            image_array = np.array(image).reshape((1, 224, 224, 3)).astype(np.float32)
            image_array = image_array / 255.0

            model.set_tensor(input_index, image_array)
            model.invoke()
            output = model.get_tensor(output_index)

            predicted_index = np.argmax(output)
            predicted_class = labels[predicted_index]
            
            result_text.value = f"Predicted class: {predicted_class}"

            pred = predicted_class[2::]
            
            if pred in disposal_methods:
                disposal_text.value = f"Disposal Method: {disposal_methods[pred]}"
            else:
                disposal_text.value = "Disposal Method: Not found."

            image_control.src_base64 = base64.b64encode(open(file_path, "rb").read()).decode('utf-8')
            
            page.update()

    file_picker = ft.FilePicker(on_result=classify_image)
    page.overlay.append(file_picker)

    title_text = ft.Text("CleanCity: Enhancing Waste Disposal and Sanitation Through Technology", size=40, weight=ft.FontWeight.BOLD)
    instruction_text = ft.Text("Submit an image to get proper disposal method.", size=24)

    page.add(
        ft.Column([
            title_text,
            instruction_text,
            ft.ElevatedButton("Select Image", on_click=lambda _: file_picker.pick_files()),
            image_control,
            result_text,
            disposal_text
        ])
    )

ft.app(target=main)