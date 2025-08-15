from utils.counter import count_vehicles
from utils.downloader import download_video
from utils.detector import detect_and_display

# Main function to download video and perform detection
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=MNn9qKG2UFI"

    # Download video from YouTube
    video_path = download_video(video_url)

    # Perform vehicle detection and display results
    # detect_and_display(video_path)

    # Count vehicles in the video and save results to CSV
    count_vehicles(video_path)
