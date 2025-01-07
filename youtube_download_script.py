import os  # Importing the os module to execute system commands

def download_youtube():
    # Prompt the user to enter the YouTube video URL
    url = input("Enter the YouTube video URL: ")
    
    # Ask the user if they want to download video or audio
    choice = input("Download video or audio? (v/a): ").lower()

    # Prompt the user to enter the download folder path
    download_path = input("Enter the download folder path (or press Enter for current directory): ").strip()

    # If the user doesn't enter a path, use the current directory
    if not download_path:
        download_path = "."  # The '.' represents the current working directory

    # If the user chooses video
    if choice == 'v':
        # Use the yt-dlp command to download the best video and audio streams
        os.system(f'yt-dlp -f bestvideo+bestaudio -P "{download_path}" {url}')
    # If the user chooses audio
    elif choice == 'a':
        # Use the yt-dlp command to download the best audio stream
        os.system(f'yt-dlp -f bestaudio -P "{download_path}" {url}')
    # If the user enters an invalid choice
    else:
        print("Invalid choice. Enter 'v' for video or 'a' for audio.")

# Run the function when the script is executed
if __name__ == "__main__":
    download_youtube()
