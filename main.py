import cv2
import numpy as np
from ultralytics import YOLO

def extract_document_boundary(image_path, model_path, output_path):
    print(f"Loading image from {image_path}...")
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read the image at {image_path}")
        
    original_h, original_w = img.shape[:2]
    
    print(f"Loading YOLO segmentation model from {model_path}...")
    model = YOLO(model_path)
    
    results = model.predict(source=img, conf=0.1, save=False, verbose=False)
    print("Results:", results)
    
    if hasattr(results[0], 'boxes') and results[0].boxes is not None:
        boxes = results[0].boxes.xywh.cpu().numpy()
        print("Detected boxes:", boxes)
    else:
        print("No bounding boxes detected.")
        return

    for box in boxes:
        x_center, y_center, width, height = box
        x1 = int(x_center - width / 2)
        y1 = int(y_center - height / 2)
        x2 = int(x_center + width / 2)
        y2 = int(y_center + height / 2)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imwrite(output_path, img)
    print(f"Successfully processed. Output saved to: {output_path}")

extract_document_boundary(
    'C:\\Users\\sanket jadhav\\OneDrive\\Desktop\\python\\input.jpeg',
    'yolov8n-seg.pt',
    'C:\\Users\\sanket jadhav\\OneDrive\\Desktop\\python\\output_rectified.jpg'
)
