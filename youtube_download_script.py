import os

def download_youtube():
    url = input("Enter the YouTube video URL: ")
    choice = input("Download video or audio? (v/a): ").lower()

    # Prompt user for download location
    download_path = input("Enter the download folder path (or press Enter for current directory): ").strip()
    if not download_path:
        download_path = "."  # Use current directory if no input is provided

    if choice == 'v':
        os.system(f'yt-dlp -f bestvideo+bestaudio -P "{download_path}" {url}')
    elif choice == 'a':
        os.system(f'yt-dlp -f bestaudio -P "{download_path}" {url}')
    else:
        print("Invalid choice. Enter 'v' or 'a'.")

if __name__ == "__main__":
    download_youtube()
