Identity Document Boundary Extraction

This project uses YOLOv8 segmentation to detect the boundaries of identity card-like objects (such as a driver’s license, passport, etc.) in an image. The process includes detecting the document's boundaries, applying a perspective transformation to straighten the document, and saving the rectified output.

Table of Contents

Overview

Requirements

Installing Dependencies

Required Libraries

YOLOv8 Model

Model File

Download YOLOv8 Model

Project Structure

Running the Script

Command to Run

Example

Expected Output

Troubleshooting

Model Not Found

No Bounding Boxes Detected

Error: 'list' object has no attribute 'masks'

License

Overview

The goal of this project is to detect and rectify the boundaries of an identity card-like object in an image. It uses the YOLOv8 model for object detection, specifically for detecting documents. The script performs the following steps:

Detects the document: YOLOv8 identifies the boundaries of the document in the image.

Applies perspective correction: If the document is tilted, the script straightens it using a perspective transformation.

Saves the output: The rectified document is saved as a new image file.

Requirements
Installing Dependencies

Before running the script, you need to install the required Python libraries. The easiest way to install all dependencies is by using the requirements.txt file.

Clone or download the project.

Navigate to the project directory where the requirements.txt file is located.

Run the following command to install all required dependencies:

pip install -r requirements.txt
Required Libraries

The project requires the following Python libraries:

opencv-python: For image processing tasks like loading, manipulating, and displaying images.

numpy: For handling numerical operations, especially for manipulating image arrays.

ultralytics: For using the YOLOv8 model for object detection and segmentation.

If you prefer to install the libraries individually, use the following commands:

pip install opencv-python
pip install numpy
pip install ultralytics
YOLOv8 Model

This script uses the YOLOv8 segmentation model to detect the document. The YOLO (You Only Look Once) architecture is one of the most powerful deep learning models for real-time object detection.

Model File

The model file used in this project is yolov8n-seg.pt, which is the lightweight version of the YOLOv8 segmentation model. It is trained to detect objects in images and create segmentation masks for them.

Download YOLOv8 Model

If the model file (yolov8n-seg.pt) is not available locally, the script will try to download it automatically from the Ultralytics repository.

You can also manually download the model from the official YOLO repository
 and save it as yolov8n-seg.pt.

Project Structure

Here is the structure of the project:

/identity-document-boundary-extraction
│
├── main.py                       # Main script to process document boundaries
├── yolov8n-seg.pt                # Pre-trained YOLOv8 segmentation model (if not auto-downloading)
├── input_image.jpg               # Example input image
├── output_image.jpg              # Rectified output image
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
Files:

main.py: The main script that contains the logic for document boundary extraction and rectification.

yolov8n-seg.pt: The pre-trained YOLOv8 model used for object detection and segmentation.

input_image.jpg: An example image file (replace this with your own image for processing).

output_image.jpg: The rectified document image will be saved here after processing.

Running the Script
Command to Run

After installing the dependencies and ensuring the model is available, you can run the script using the following command:

python main.py --input "C:\path\to\input_image.jpg" --output "C:\path\to\output_rectified.jpg" --model "C:\path\to\yolov8n-seg.pt"
Example:

If you want to run the script using the image located at:

Input image path: C:\Users\sanket jadhav\OneDrive\Desktop\python\Domicile Cer.jpg

Model file path: yolov8n-seg.pt

Output image path: C:\Users\sanket jadhav\OneDrive\Desktop\python\output_rectified.jpg

Use this command:

python main.py --input "C:\Users\sanket jadhav\OneDrive\Desktop\python\Domicile Cer.jpg" --output "C:\Users\sanket jadhav\OneDrive\Desktop\python\output_rectified.jpg" --model "yolov8n-seg.pt"
Expected Output

Once the script is executed successfully:

The document boundaries will be detected using the YOLOv8 model.

Perspective transformation will be applied to rectify the document if it's tilted or skewed.

The rectified output image will be saved to the specified output path (output_rectified.jpg).

Troubleshooting
Model Not Found

If the YOLOv8 model (yolov8n-seg.pt) is not found, the script will try to download it automatically. Ensure that your machine has internet access to complete the download.

If you prefer, you can manually download the model from the official Ultralytics repository and place it in the project directory.

No Bounding Boxes Detected

If you see the message No bounding boxes detected, it means that YOLOv8 was unable to detect any documents in the image. This could be due to:

Low-quality input image: Try using a higher-resolution image.

Incorrect model: Ensure that the YOLOv8 model used is appropriate for document detection.

Document occlusion or angle: Try using a different image or adjust the model parameters.

Error: 'list' object has no attribute 'masks'

This error occurs when the model returns bounding boxes but not segmentation masks. You can either:

Modify the code to work with bounding boxes instead of segmentation masks (already implemented in the script).

Use a different model that provides segmentation masks.

License

This project is open-source and available under the MIT License. Feel free to contribute or use it for your projects.
