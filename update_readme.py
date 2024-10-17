import feedparser
import re
import sys


def fetch_blog_posts():
    print("Fetching blog posts...")
    feed_url = "https://andypiper.co.uk/feed/"  # Updated to your actual feed URL
    feed = feedparser.parse(feed_url)
    posts = feed.entries[:5]  # Get the 5 most recent posts
    print(f"Fetched {len(posts)} posts")
    for post in posts:
        print(f"- {post.title} ({post.get('published', 'No date')})")
    return posts


def update_readme(posts):
    print("Updating README.md...")
    try:
        with open("README.md", "r") as file:
            old_content = file.read()
        print("README.md content loaded")

        # Define the markers for the blog posts section
        start_marker = "<!-- BLOG-POST-LIST:START -->"
        end_marker = "<!-- BLOG-POST-LIST:END -->"

        # Create the new blog posts list
        new_posts_content = "\n".join(
            [
                f"- [{post.title}]({post.link})"
                for post in posts
            ]
        )
        print("New posts content created:")
        print(new_posts_content)

        # Extract the old posts content
        old_posts_content = re.search(
            f"{start_marker}(.*?){end_marker}", old_content, re.DOTALL
        )
        if old_posts_content:
            old_posts_content = old_posts_content.group(1).strip()
            print("Old posts content:")
            print(old_posts_content)

        # Replace the content between the markers
        new_content = re.sub(
            f"{start_marker}.*?{end_marker}",
            f"{start_marker}\n{new_posts_content}\n{end_marker}",
            old_content,
            flags=re.DOTALL,
        )

        if new_content == old_content:
            print("No changes detected in README content")
            return False

        print("Content difference detected. Updating file...")
        with open("README.md", "w") as file:
            file.write(new_content)
        print("README.md updated successfully")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


if __name__ == "__main__":
    print("Script started")
    posts = fetch_blog_posts()
    if update_readme(posts):
        print("README updated")
        sys.exit(0)
    else:
        print("No changes made to README")
        sys.exit(1)
