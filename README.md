# CleanCity: Enhancing Waste Disposal and Sanitation Through Technology

## Overview

The CleanCity Application is a user-friendly tool designed to help users identify the proper disposal methods for various types of waste. By leveraging machine learning and image processing, this application allows users to upload an image of waste, which is then classified, and the corresponding disposal method is provided.

## Features

- **Image Classification**: Uses a TensorFlow Lite model to classify waste types from uploaded images.
- **Disposal Methods**: Provides users with proper disposal methods based on the classification results.
- **User-Friendly Interface**: Built with Flet for an interactive and responsive user experience.
- **Lightweight**: The application runs efficiently on local machines without requiring heavy resources.

## Technologies Used

- **Flet**: A framework for building interactive web applications in Python.
- **TensorFlow Lite**: A lightweight version of TensorFlow designed for mobile and edge devices, used for running the machine learning model.
- **Pillow (PIL)**: A Python Imaging Library used for image processing.
- **NumPy**: A library for numerical operations in Python.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Anirudhabg/CleanCity.git
   cd CleanCity
   ```
2. Create a flet app.

    ```bash
    flet create app
    cd app
    ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have the TensorFlow Lite model (`model_unquant.tflite`) and labels file (`labels.txt`) in the project directory.

5. Prepare the `waste.csv` file containing waste types and their corresponding disposal methods.

## Usage

1. Run the application:

   ```bash
   flet run .\main.py
   ```

2. Click on "Select Image" to upload an image of waste.

3. The application will display the predicted class of waste along with the recommended disposal method.

## Images
This is the startup page

![Start Up Page](https://github.com/Anirudhabg/CleanCity/blob/166575fd2df0aaf1fae495746ff56190037de331/Images/StartUp.png)

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.