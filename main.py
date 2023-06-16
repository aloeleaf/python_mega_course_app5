import requests

api_key = "4990955fc62b4ce7a32c952b8d7ec4ef"

url= "https://newsapi.org/v2/everything?q=tesla" \
     "&from=2023-05-16&sortBy=publishedAt" \
     "&apiKey=4990955fc62b4ce7a32c952b8d7ec4ef"

# Make request
request = requests.get(url)

# Get a dicionary with data
content = request.json()

# Access the articles and description
for article in content["articles"]:
    print((article["title"]))

