def format_post(summary_text, article_link, article_image=None):
    """
    Converts summary into social media-ready caption:
    - Hook line
    - Short summary (1-2 lines)
    - Hashtags
    - Call-to-action with article link
    - Image reference
    """
    # Hook line
    hook = "🚀 Latest Drone News!"
    
    # Short summary (truncate if too long)
    short_summary = summary_text
    if len(summary_text) > 250:
        short_summary = summary_text[:247] + "..."
    
    # Example hashtags (could be extracted dynamically in future)
    hashtags = "#DroneNews #UAV #DroneTech #Drones"
    
    # Call-to-action with article link
    cta = f"Read more here: {article_link}"
    
    # Include image reference if provided
    image_ref = f"Attached image: {article_image}" if article_image else ""
    
    post = f"{hook}\n\n{short_summary}\n\n{hashtags}\n{cta}\n{image_ref}"
    return post

# Test
if __name__ == "__main__":
    summary = "Drones are transforming logistics in India by enabling faster deliveries and improving efficiency across multiple sectors."
    post = format_post(summary, "https://example.com", "screenshots/sample.png")
    print(post)
