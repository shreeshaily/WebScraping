import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://thehackernews.com/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all("div", class_="body-post")

data = []

for post in posts:
    # Title
    title_tag = post.find("h2", class_="home-title")
    title = title_tag.text.strip() if title_tag else "N/A"

    # Link
    link_tag = title_tag.find("a") if title_tag else None
    link = link_tag["href"] if link_tag else "N/A"

    # Date
    date_tag = post.find("span", class_="h-datetime")
    date = date_tag.text.strip() if date_tag else "N/A"

    # Author
    author_tag = post.find("span", class_="h-author")
    author = author_tag.text.strip() if author_tag else "N/A"

    # Summary
    summary_tag = post.find("div", class_="home-desc")
    summary = summary_tag.text.strip() if summary_tag else "N/A"

    data.append([title, date, author, link, summary])

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=["Title", "Date", "Author", "Link", "Summary"]
)

# Save to CSV
df.to_csv("hacker_news.csv", index=False, encoding="utf-8")

print("✅ CSV file created with", len(df), "records")
