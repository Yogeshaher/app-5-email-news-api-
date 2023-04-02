import requests
from send_email import send_email

topic = "tesla"
api_key = "307b7d5c6f964d939792bd561d3380c4"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
    "from=2023-03-02&sortBy=publishedAt" \
      "&apiKey=307b7d5c6f964d939792bd561d3380c4&" \
    "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's News" + "\n" + body + article["title"] + "\n" + \
               article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)