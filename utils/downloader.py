import os
import yt_dlp

# download video from YouTube using yt-dlp
def download_video(url, filename="traffic.mp4"):
    """
    Downloads YouTube video using yt-dlp if not already downloaded.
    """
    if os.path.exists(filename):
        # If file already exists, skip download
        print(f"{filename} already exists. Skipping download.")
        return filename
    
    print("Downloading video using yt-dlp...")
    ydl_opts = {
        'outtmpl': filename,
        'format': 'mp4'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return filename
