import newspaper

# Declare the url
url = "https://ktechhub.com/tutorials/completely-deploy-your-laravel-application-on-ubuntu-linux-server-60a51098a8bf2"

#Extract web content
url = newspaper.Article(url="%s" % (url), language='en')

url.download()
url.parse()

# Display scraped data
print(url.text)
