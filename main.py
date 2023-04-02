import requests

api_key = "307b7d5c6f964d939792bd561d3380c4"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-03-02& " \
    "sortBy=publishedAt" \
    "&apiKey=307b7d5c6f964d939792bd561d3380c4"

# make request
request =requests.get(url)

# get a dictionary with data
content = request.json()

# access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])


