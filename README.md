Identity Document Boundary Extraction

This project uses YOLOv8 segmentation to detect the boundaries of identity card-like objects (e.g., driver’s license, passport) in an image. It performs boundary detection, applies a perspective transformation to straighten the document, and saves the rectified output.

Table of Contents

Overview

Requirements

YOLOv8 Model

Project Structure

Running the Script

Expected Output

Troubleshooting

License

Overview

This project detects the boundaries of a document in an image using YOLOv8, applies a perspective transformation to rectify it, and saves the rectified document.

Requirements
Install Dependencies

Run the following command to install all dependencies:

pip install -r requirements.txt
Required Libraries

opencv-python: Image processing.

numpy: Numerical operations.

ultralytics: YOLOv8 model for object detection.

YOLOv8 Model

This script uses YOLOv8 for object detection. The model file used is yolov8n-seg.pt.

Model File: yolov8n-seg.pt (lightweight YOLOv8 segmentation model).

Download: The model will automatically download if not available locally. You can also manually download it from the official Ultralytics repository
.

Project Structure
/identity-document-boundary-extraction
│
├── main.py                  # Script to process document boundaries
├── yolov8n-seg.pt           # YOLOv8 model (if not auto-downloading)
├── input_image.jpg          # Example input image
├── output_image.jpg         # Rectified output image
├── requirements.txt         # Dependencies
└── README.md                # Documentation
Running the Script
Command to Run
python main.py --input "C:\path\to\input_image.jpg" --output "C:\path\to\output_rectified.jpg" --model "C:\path\to\yolov8n-seg.pt"
Example
python main.py --input "C:\Users\sanket jadhav\OneDrive\Desktop\python\Domicile Cer.jpg" --output "C:\Users\sanket jadhav\OneDrive\Desktop\python\output_rectified.jpg" --model "yolov8n-seg.pt"
Expected Output

The rectified document image will be saved at the specified output path (output_rectified.jpg).

Troubleshooting

Model Not Found: Ensure internet access for downloading the model or manually download it from the official repository.

No Bounding Boxes Detected: Try using a higher-quality image, or adjust the model and image parameters.

Error: 'list' object has no attribute 'masks': Modify the code to use bounding boxes instead of segmentation masks.

License

This project is open-source and available under the MIT License.
