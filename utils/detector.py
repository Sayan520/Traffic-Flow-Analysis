import cv2
from ultralytics import YOLO

# load once globally
model = YOLO("yolov8n.pt")

# Define vehicle classes based on COCO dataset (car, motorcycle, bus, truck)
VEHICLE_CLASSES = [2, 3, 5, 7]  

# detect vehicles in a video & shows bounding boxes in real-time
def detect_and_display(video_path):
    """
    Detects vehicles in a video and shows bounding boxes in real-time.
    """
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]
        print(f"Detected {len(results.boxes)} objects")

        for box in results.boxes:
            cls = int(box.cls[0])
            if cls in VEHICLE_CLASSES:
                x1, y1, x2, y2 = box.xyxy[0]
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                label = model.names[cls]
                cv2.putText(frame, label, (int(x1), int(y1)-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Vehicle Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
