# utils.py
import requests

def download_image(image_url, save_path):
    """
    Downloads image from a URL.
    """
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
            return save_path
        else:
            print("Failed to download image")
            return None
    except Exception as e:
        print("Error:", e)
        return None

# Test
if __name__ == "__main__":
    download_image("https://via.placeholder.com/150", "screenshots/test.png")
