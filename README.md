# CleanCity: Enhancing Waste Disposal and Sanitation Through Technology

## Overview

CleanCity is an innovative application designed to improve urban waste management. It helps users identify the proper disposal methods for different types of waste, allows them to report trash-related issues, and provides a real-time task management system for garbage collectors.

## Features

- **Waste Disposal Information**: Get detailed disposal methods for various types of waste.
- **Complaint Registration**: Report areas with excessive trash directly through the app.
- **Real-Time Task Management for Garbage Collectors**: Garbage collectors receive real-time tasks, can view reported trash locations, and update the status of their tasks.

## Technologies Used

- **Flet**: A framework for building interactive web applications in Python.
- **TensorFlow Lite**: A lightweight version of TensorFlow designed for mobile and edge devices, used for running the machine learning model.
- **Pillow (PIL)**: A Python Imaging Library used for image processing.
- **NumPy**: A library for numerical operations in Python.


## Installation

To set up the CleanCity application locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Anirudhabg/CleanCity.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd CleanCity
   ```

3. **Install Requirements**:
   Create a `requirements.txt` file with the following content if it doesn't already exist:
   ```plaintext
   tensorflow
   flet
   pillow
   numpy
   ```
   Then, run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to the User Directory**:
   Open a terminal and run:
   ```bash
   cd User
   ```

5. **Run the User Application**:
   In the same terminal, execute:
   ```bash
   flet run main.py
   ```

6. **Open Another Terminal** and **Navigate to the Garbage Collector Directory**:
   ```bash
   cd GarbageCollector
   ```

7. **Run the Garbage Collector Application**:
   In this new terminal, execute:
   ```bash
   flet run main.py
   ```

Make sure you have TensorFlow Lite models, labels, and other required files in their respective directories as specified in your script.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
