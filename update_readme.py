import feedparser
import re


def fetch_blog_posts():
    print("Fetching blog posts...")
    feed_url = (
        "https://andypiper.co.uk/feed/"
    )
    feed = feedparser.parse(feed_url)
    posts = feed.entries[:5]  # Get the 5 most recent posts
    print(f"Fetched {len(posts)} posts")
    for post in posts:
        print(f"- {post.title} ({post.published.split('T')[0]})")
    return posts


def update_readme(posts):
    print("Updating README.md...")
    with open("README.md", "r") as file:
        content = file.read()
    print("README.md content loaded")

    # Define the markers for the blog posts section
    start_marker = "<!-- BLOG-POST-LIST:START -->"
    end_marker = "<!-- BLOG-POST-LIST:END -->"

    # Create the new blog posts list
    new_content = "\n".join(
        [
            f"- [{post.title}]({post.link}) - {post.published.split('T')[0]}"
            for post in posts
        ]
    )
    print("New content created:")
    print(new_content)

    # Replace the content between the markers
    pattern = f"{start_marker}.*?{end_marker}"
    replacement = f"{start_marker}\n{new_content}\n{end_marker}"
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    print("Content replaced")

    with open("README.md", "w") as file:
        file.write(updated_content)
    print("README.md updated successfully")


if __name__ == "__main__":
    print("Script started")
    posts = fetch_blog_posts()
    update_readme(posts)
    print("Script completed")
