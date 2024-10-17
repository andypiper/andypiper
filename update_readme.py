import feedparser

# Fetch the RSS feed
feed_url = "https://andypiper.co.uk/feed/"
feed = feedparser.parse(feed_url)

# Extract the latest 5 posts
max_posts = 5
latest_posts = []
for entry in feed.entries[:max_posts]:
    title = entry.title
    link = entry.link
    latest_posts.append(f"- [{title}]({link})")

# Read the existing README.md content
with open("README.md", "r") as readme_file:
    readme_content = readme_file.readlines()

# Find the marker where blog posts should be inserted
start_marker = "<!-- BLOG-POST-LIST:START -->\n"
end_marker = "<!-- BLOG-POST-LIST:END -->\n"

# Ensure the markers are present in the README.md
if start_marker not in readme_content or end_marker not in readme_content:
    print("Markers not found in README.md. Please ensure you have the markers.")
    exit(1)

# Get the content before and after the markers
start_index = readme_content.index(start_marker) + 1
end_index = readme_content.index(end_marker)

# Create the new content between the markers
new_readme_content = (
    readme_content[:start_index]
    + [f"{post}\n" for post in latest_posts]
    + readme_content[end_index:]
)

# Write the new content back to README.md
with open("README.md", "w") as readme_file:
    readme_file.writelines(new_readme_content)

print("README.md has been updated with the latest blog posts.")
