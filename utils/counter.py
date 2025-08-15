import cv2
import pandas as pd
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Only these classes are counted as vehicles
VEHICLE_CLASSES = [2, 3, 5, 7] 

# LANE definitions based on your video width (640px)
LANES = {
    1: (0, 213),      
    2: (214, 426),    
    3: (427, 640),    
}

# decide which lane a vehicle belongs to based on its center x-coordinate
def decide_lane(x_center):
    for lane_no, (l, r) in LANES.items():
        if l <= x_center <= r:
            return lane_no
    return None

# Count vehicles in the video and save results to CSV
def count_vehicles(video_path, save_csv=True):
    cap = cv2.VideoCapture(video_path)
    frame_id = 0

    # live count trackers
    counted_ids = {1: set(), 2: set(), 3: set()}
    output = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_id += 1

        # run YOLO in tracking mode
        results = model.track(frame, persist=True)[0]
        # print the number of detections in the current frame
        print(f"Processing frame {frame_id}... and found {len(results.boxes)} detections") 

        for box in results.boxes:
            cls = int(box.cls[0])
            if cls in VEHICLE_CLASSES:
                x1, y1, x2, y2 = box.xyxy[0]
                vehicle_id = int(box.id[0]) if box.id is not None else None

                centerx = int((x1 + x2) / 2)
                lane_no = decide_lane(centerx)

                # draw lane boundaries
                for lane, (left, right) in LANES.items():
                    cv2.line(frame, (left, 0), (left, frame.shape[0]), (255, 0, 0), 2)
                    cv2.putText(frame, f"Lane {lane}", (left + 5, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

                # draw detection box
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

                # count when first seen in a lane
                if vehicle_id is not None and lane_no:
                    if vehicle_id not in counted_ids[lane_no]:
                        counted_ids[lane_no].add(vehicle_id)
                        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
                        output.append([vehicle_id, lane_no, frame_id, timestamp])

        # === LIVE COUNT OVERLAY === #
        overlay_text = (
            f"Lane1: {len(counted_ids[1])}  "
            f"Lane2: {len(counted_ids[2])}  "
            f"Lane3: {len(counted_ids[3])}"
        )
        cv2.putText(frame, overlay_text, (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 3)

        cv2.imshow("Lane Counting", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if save_csv:
        df = pd.DataFrame(output, columns=["VehicleID", "LaneNo", "Frame", "Timestamp"])
        df.to_csv("lane_counts.csv", index=False)
        print("CSV saved as lane_counts.csv")

    # summary print
    for lane in [1, 2, 3]:
        print(f"Total in Lane {lane} :", len(counted_ids[lane]))
