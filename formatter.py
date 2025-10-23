# formatter.py
def format_post(summary_text, article_link):
    """
    Converts summary into social media caption:
    - Hook line
    - Short summary
    - Hashtags
    - Call-to-action with article link
    """
    # Simple formatting example
    hook = "🚀 Latest Drone News!"
    hashtags = "#DroneNews #UAV #DroneTech"
    post = f"{hook}\n\n{summary_text}\n\n{hashtags}\nRead more: {article_link}"
    return post

# Test
if __name__ == "__main__":
    summary = "Drones are transforming logistics in India..."
    post = format_post(summary, "https://example.com")
    print(post)
