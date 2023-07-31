import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import openai

# OPENAI
openai.api_key = 'YOUR_CHATGPT_API_KEY'

# newsource
news_url = "https://news.google.com/news/rss"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()

# getting top 5 news articles
soup_page = soup(xml_page, "xml")
news_list = soup_page.findAll("item")

# Generate slogans using the ChatGPT API for each news headline
for news in news_list[0:5]:
    #prompt to get the birthday slogan
    messages = [{"role": "system", "content": "You are a program that takes each news headlines and comes up with 1 short rude and whitty slogans for that to put on a birthday card or cards for other occasions"},
                {"role": "user", "content": news.title.text}]
    
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content

    #reply to get image prompt
    messages = [{"role": "system", "content": "You are a program that takes each news slogan and comes up with a prompt to put into an image generation tool to create a handpanted comical design for a birthday card"},
                {"role": "user", "content": reply}]
    
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    prompt = chat.choices[0].message.content

    print(news.title.text)
    print(f"Slogan: {reply}")
    print(f"Prompt: {prompt}")
    print("-" * 60)
