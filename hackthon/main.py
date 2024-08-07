import cv2
from src.video_input import VideoCapture
from src.light_assessment import assess_light_condition
from src.low_light_enhancement import enhance_image_clahe
from src.object_detection import YOLOv8
from src.tracking import DeepSortTracker
from src.activity_recognition import ActivityRecognizer
from src.alert_system import send_email_alert, send_sms_alert

def main():
    cap = VideoCapture(0)
    yolo = YOLOv8("models/yolov8n.pt")
    deepsort = DeepSortTracker()
    activity_recognizer = ActivityRecognizer()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        light_condition = assess_light_condition(frame)
        if light_condition == 'Low':
            frame = enhance_image_clahe(frame)

        detections = yolo.detect(frame)
        tracks = deepsort.update(detections, frame)

        for track in tracks:
            bbox = track.to_tlbr()
            cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (255, 0, 0), 2)
            cv2.putText(frame, str(track.track_id), (int(bbox[0]), int(bbox[1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # Example: if a suspicious activity is detected, send alerts
        # if activity_recognizer.is_suspicious(frame):
        #     send_email_alert('Suspicious activity detected at the front door.')
        #     send_sms_alert('Suspicious activity detected at the front door.')

        cv2.imshow('Surveillance', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
