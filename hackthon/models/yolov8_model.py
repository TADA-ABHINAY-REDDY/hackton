# yolov8_model.py

import torch

class YOLOv8Model:
    def __init__(self, model_path='models/yolov8n.pt'):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
        self.model.eval()

    def detect(self, image):
        results = self.model(image)
        return results
