import requests
import send_mail


api_key = "4990955fc62b4ce7a32c952b8d7ec4ef"

url= "https://newsapi.org/v2/everything?q=tesla" \
     "&from=2023-05-16&sortBy=publishedAt" \
     "&apiKey=4990955fc62b4ce7a32c952b8d7ec4ef"

# Make request
request = requests.get(url)

# Get a dicionary with data
content = request.json()

message = str()

# Access the articles and description
for articles in content["articles"]:
    if articles["title"] is not None:
     #message += f'Article Title: {articles["title"]} \n\nArticle Description: {articles["description"]} \n\n\n\n'
     message = message +  articles["title"] + "\n" + articles["description"] + 2*"\n"

send_mail.send_mail(message, "sandorsz@birosag.hu") 
