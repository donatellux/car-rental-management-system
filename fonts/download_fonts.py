import os
import urllib.request

def download_file(url, filename):
    """Download a file from URL to the specified filename"""
    print(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

def main():
    # Create fonts directory if it doesn't exist
    if not os.path.exists("fonts"):
        os.makedirs("fonts")

    # Font URLs
    fonts = {
        "NotoSans-Regular.ttf": "https://github.com/googlefonts/noto-fonts/raw/main/hinted/ttf/NotoSans/NotoSans-Regular.ttf",
        "NotoSansArabic-Regular.ttf": "https://github.com/googlefonts/noto-fonts/raw/main/hinted/ttf/NotoSansArabic/NotoSansArabic-Regular.ttf"
    }

    # Download each font
    for filename, url in fonts.items():
        filepath = os.path.join("fonts", filename)
        if not os.path.exists(filepath):
            download_file(url, filepath)
        else:
            print(f"{filename} already exists")

if __name__ == "__main__":
    main()
