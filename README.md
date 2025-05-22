# CleanCity: Enhancing Waste Disposal and Sanitation Through Technology

## Overview

**CleanCity** is an innovative application designed to improve urban waste management. It empowers users to properly identify and dispose of waste while enabling authorities to handle sanitation tasks more efficiently. The application also provides real-time task management for garbage collectors, enhancing communication and coordination.

## Features

- 🗑️ **Waste Disposal Information**: Get accurate and detailed guidance on disposing of different types of waste.
- 📸 **Complaint Registration**: Capture and report trash-related issues using the app’s built-in functionality.
- ⚙️ **Real-Time Task Management for Garbage Collectors**: Garbage collectors receive tasks, view complaint locations, and update progress in real-time.

## Technologies Used

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Flet](https://img.shields.io/badge/Flet-UI%20Framework-blueviolet?logo=python)](https://flet.dev/)
[![TensorFlow Lite](https://img.shields.io/badge/TensorFlow_Lite-ML-orange?logo=tensorflow)](https://www.tensorflow.org/lite)
[![Pillow](https://img.shields.io/badge/Pillow-Image_Processing-yellow?logo=python)](https://python-pillow.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-blue?logo=numpy)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-black?logo=pandas)](https://pandas.pydata.org/)
[![JSON](https://img.shields.io/badge/JSON-Data_Format-lightgrey?logo=json)](https://www.json.org/)


## Installation

To set up the CleanCity application locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/Anirudhabg/CleanCity.git
cd CleanCity
````

### 2. Install Dependencies

If `requirements.txt` does not exist, create one with:

```txt
tensorflow
flet
pillow
numpy
```

Then run:

```bash
pip install -r requirements.txt
```

### 3. Run the User Module

```bash
cd User
flet run main.py
```

### 4. Run the Garbage Collector Module

Open another terminal:

```bash
cd GarbageCollector
flet run main.py
```

> 🔍 Ensure that the TensorFlow Lite model (`model_unquant.tflite`), label file (`label.txt`), and data file (`waste.csv`) are present in the **User** directory.

## Project Structure

```
CleanCity/
│
├── Complaints/
│   └── complaints.json
│
├── GarbageCollector/
│   ├── assets/
│   └── main.py
│
├── User/
│   ├── assets/
│   ├── main.py
│   ├── model_unquant.tflite
│   ├── label.txt
│   └── waste.csv
│
└── README.md
```

## Module Screenshots

| User Module                                                                                   | Garbage Collector Module                                                                                             |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| ![User Module](https://github.com/Anirudhabg/CleanCity/blob/503eccc5d20d0a84fda156c4309682f4af0465aa/1.png) | ![Garbage Collector Module](https://github.com/Anirudhabg/CleanCity/2.png) |

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
> Crafted by Anirudha B G Somayaji
