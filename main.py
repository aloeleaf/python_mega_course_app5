import requests
import send_mail


api_key = "4990955fc62b4ce7a32c952b8d7ec4ef"
topic = "tesla"

url= "https://newsapi.org/v2/everything?" \
     f"q={topic}" \
     "&from=2023-05-16" \
     "&sortBy=publishedAt" \
     "&apiKey=4990955fc62b4ce7a32c952b8d7ec4ef" \
     "&language=en"

# Make request
request = requests.get(url)

# Get a dicionary with data
content = request.json()

message = str()

# Access the articles and description
for article in content["articles"][:20]:
    if article["title"] is not None:
     message += "Subject: Today's news" + "\n" \
                + article["title"] + "\n" \
                + article["description"] + "\n" \
                + article["url"] + "\n" + 2*"\n"

send_mail.send_mail(message, "sandorsz@birosag.hu") 
