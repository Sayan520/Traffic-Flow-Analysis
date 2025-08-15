# Traffic Flow Analysis – Vehicle Detection and Lane-wise Counting (Computer Vision)

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

# (optional) create venv:
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
├── main.py
├── requirements.txt
├── README.md
└── utils/
    ├── __init__.py
    ├── downloader.py
    ├── detector.py
    └── counter.py
```

## 🎥 Demo Video

> (Attach or upload your screen recording link here)

## ✍️ Author / Contact

**Your Name** – for interview assignment

