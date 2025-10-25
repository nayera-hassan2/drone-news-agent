import os

def post_to_social_media(post_text, image_path=None):
    """
    Simulates posting content to social media platforms.
    Picks image automatically if provided.
    """
    print("Posting to social media...")
    print(post_text)
    if image_path:
        print(f"Attached image: {image_path}")

# Test
if __name__ == "__main__":
    post_text = "🚀 Latest Drone News!\n\nDrones are transforming logistics in India...\n\n#DroneNews #UAV #DroneTech\nRead more here: https://example.com"
    post_to_social_media(post_text, "screenshots/sample.png")
