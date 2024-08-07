from ultralytics import YOLO

class YOLOv8:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame)
        detections = [[det.xyxy[0][0].item(), det.xyxy[0][1].item(), det.xyxy[0][2].item(), det.xyxy[0][3].item(), det.conf[0].item(), det.cls[0].item()] for det in results[0]]
        return detections
