# Identity Document Boundary Extraction

This project uses YOLOv8 segmentation to detect and rectify the boundaries of identity card-like objects (such as a driver’s license, passport, etc.) from input images. The process involves detecting the boundaries, applying a perspective transformation to straighten the document, and saving the rectified output.

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.6 or higher
- `pip` to install required packages

### Install Dependencies

You can install the required dependencies by using the following command:

```bash
pip install -r requirements.txt
