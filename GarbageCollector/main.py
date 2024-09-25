import flet as ft
import json
import os
import threading
import time
import datetime

date = datetime.datetime.now().strftime("%d - %m - %Y")
# Path to the complaints file
complaints_file_path = (
    "C:/Users/LENOVO/Documents/GitHub/CleanCity/Complaints/complaints.json"
)


# Function to load complaints from the JSON file
def load_complaints():
    if os.path.exists(complaints_file_path):
        with open(complaints_file_path, "r") as file:
            try:
                data = (
                    file.read().strip()
                )  # Read the file and strip any extra whitespace
                if data:
                    return json.loads(data)  # Load JSON if file has content
                else:
                    return []  # If file is empty, return an empty list
            except json.JSONDecodeError:
                return []  # If file contains invalid JSON, return an empty list
    return []  # If file doesn't exist, return an empty list


# Function to mark a complaint as completed
def complete_task(page, task_id):
    complaints = load_complaints()
    complaints[task_id]["status"] = "Completed"

    # Update the status in the simulated database
    with open(complaints_file_path, "w") as file:
        json.dump(complaints, file)

    page.snack_bar = ft.SnackBar(ft.Text(f"Task {task_id + 1} marked as completed!"))
    page.snack_bar.open = True
    refresh_complaints(page)


# Function to refresh the complaints/task list
def refresh_complaints(page):
    complaints = load_complaints()
    tasks.controls.clear()
    for i, task in enumerate(complaints):
        tasks.controls.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(f"Task {i + 1}",size=20),
                        ft.Text(f"User: {task['user']}", style="headline6"),
                        ft.Text(f"Complaint: {task['complaint']}", style="body1"),
                        ft.Row(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text(f"Phone Number: {task['phone_number']}", style="body2"),
                                        ft.Text(f"Email: {task['email']}", style="body2"),
                                        ft.Text(f"Status: {task['status']}", style="body2"),
                                        ft.Text(f"Location: {task['location']}", style="body2"),
                                    ]
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                    ],
                ),
                padding=8,
                margin=4,
                border=ft.border.all(2,ft.colors.WHITE),
                border_radius=ft.border_radius.all(8),
                on_click=lambda e, i=i: (
                    complete_task(page, i) if task["status"] == "Pending" else None
                ),
                data=i,
            )
        )

    page.update()


# Function to periodically refresh the complaints/task list
def periodic_refresh(page):
    while True:
        refresh_complaints(page)
        time.sleep(5)  # Refresh every 5 seconds


# Main function to setup the Flet page
def main(page: ft.Page):
    page.title = "Garbage Collector - Task Management"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Regular.ttf",
    }
    page.theme = ft.Theme(font_family="Kanit")
    # Garbage collector section for viewing and managing tasks
    global tasks
    tasks = ft.Column(scroll="adaptive", spacing=50)

    # Layout for garbage collector's task list
    colm = ft.Column(
        [
            ft.Text(
                "CleanCity - Garbage Collector Application",
                size=34,
                weight=ft.FontWeight.BOLD,
            ),
            ft.Text("Garbage Collector - Task List", size=20),
            ft.Text(f"{date}",size=20),
            tasks,
        ],
        spacing=10,
        scroll=ft.ScrollMode.ALWAYS,
    )

    page.add(
        ft.Container(
            content=colm,
            width=375,
            height=667,
            border=ft.border.all(2, ft.colors.WHITE),
            padding=10,
            border_radius=ft.border_radius.all(5),
            alignment=ft.alignment.center,
        )
    )

    # Start the periodic refresh in a separate thread
    threading.Thread(target=lambda: periodic_refresh(page), daemon=True).start()

    # Initial loading of complaints/tasks
    refresh_complaints(page)


ft.app(target=main)
