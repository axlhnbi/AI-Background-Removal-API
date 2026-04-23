# AI Background Removal API 

A lightweight, high-performance REST API built with Flask that automatically removes the background from any image. Powered by the state-of-the-art `rembg` machine learning model and accelerated by ONNX Runtime.

## Key Features
* **AI-Powered:** Utilizes advanced neural networks (`rembg`) for highly accurate background matting and extraction.
* **RESTful Architecture:** Easy to integrate with any frontend (React, Vue, Android, iOS) or external services.
* **In-Memory Processing:** Uses `BytesIO` and `base64` to process images entirely in RAM without writing temporary files to the disk, ensuring blazing-fast response times.
* **Production-Ready:** Built with Flask and structured for easy deployment.

## Tech Stack
* **Python 3.8+**
* **Flask** (Web Framework)
* **rembg** (Background Removal Engine)
* **Pillow** (Image Processing)
* **ONNX Runtime** (Machine Learning Acceleration)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/axlhnbi/AI-Background-Removal-API.git
   cd bg-removal-api

2. **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (Note: The first time you run the application, rembg will automatically download the pre-trained AI model (u2net.onnx) which is             around ~170MB).

4. **Run the Server:**
    ```bash
    python app.py

## API Documentation

1. **Remove Background**
    Removes the background from an uploaded image file.

    Endpoint: /api/remove

    Method: POST

    Content-Type: multipart/form-data

    Body: * file: The image file you want to process (PNG, JPG, JPEG).

    Example Response (JSON format if using Base64 output):
    ```bash:
    {
        "status": "success",
        "message": "Background removed successfully.",
        "data": {
            "image_base64": "iVBORw0KGgoAAAANSUhEUgAA..."
        }
    }

## License
This project is open-source and available under the MIT License.
