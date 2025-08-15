# Traffic Flow Analysis – Vehicle Detection and Lane-wise Counting (Computer Vision)

<video src="https://github.com/user-attachments/assets/8f3abb33-694d-45e7-9d92-3c0c791f4a2d" width="600" autoplay loop muted></video>

## 📌 Objective

Build a Python-based system that:

- Automatically downloads a traffic video from YouTube
- Detects vehicles using a YOLOv8 pre-trained model
- Tracks vehicles across frames
- Counts vehicles in **three different lanes**
- Exports all results to a CSV file
- Displays live processed video with lane boundaries and count

## 💻 Technologies Used

| Component           | Library                |
| ------------------- | ---------------------- |
| Object Detection    | YOLOv8 (`ultralytics`) |
| Video Processing    | OpenCV                 |
| Tracking & Counting | Custom                 |
| Video Downloading   | `yt-dlp`               |
| Data Export         | Pandas                 |

## ✅ Features

- Real-time or near realtime processing
- Automatic YouTube video download
- Configurable lane boundaries
- Export CSV: Vehicle-ID, Lane-No, Frame, Timestamp
- Visual overlay for demo presentation

## 🔧 Installation

```bash
git clone https://github.com/Sayan520/Traffic-Flow-Analysis.git
cd Traffic-Flow-Analysis

# create virtual environment:
python -m venv venv
venv\Scripts\activate  # On Windows

pip install -r requirements.txt
```

## ▶️ Running the Project

```bash
python main.py
```

👉 Output:

- Live video window with detection overlay
- A `lane_counts.csv` file containing counting logs
- Summary count per lane at end

## 📊 Sample CSV Output

| VehicleID | LaneNo | Frame | Timestamp |
| --------- | ------ | ----- | --------- |
| 3         | 1      | 24    | 1.23      |
| 7         | 2      | 45    | 2.90      |
| ...       | ...    | ...   | ...       |

## 📌 Directory Structure

```
traffic_flow_analysis/
│
├── main.py           # Main script to run the analysis
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
└── utils/
    ├── __init__.py    # Optional, for package structure
    ├── downloader.py  # Downloads YouTube video
    ├── detector.py    # YOLOv8 vehicle detection
    └── counter.py     # Lane-wise counting logic
```
## 📄 Technical Summary

This system utilizes a YOLOv8 nano model pre-trained on the COCO dataset to detect vehicles in each frame of a traffic video. The frames are processed in near real time using OpenCV, and vehicle objects are tracked using the built‐in SORT tracker in YOLO to assign each a unique ID. Lane regions are defined as three vertical segments across the frame width. For every detected object, its bounding box center is used to determine which lane it belongs to. A vehicle is counted for a lane only when its ID appears for the first time in that lane to avoid duplicate counts. Each event is logged into a CSV file with the vehicle ID, lane number, frame and timestamp. A visual overlay shows lane boundaries and live per‐lane counts on the video output.

## 🎥 Demo Video

> [Watch the demo video here](https://drive.google.com/file/d/1yJPxqKwNKqPKhkQTb5WUoA3fec5QKz15/view?usp=sharing)


## ✍️ Author / Contact

**Sayan Ghosh** – ghoshsayan5205@gmail.com

