import pyshorteners

url = input('Enter the url: ')

def shortenurl(url):
    s = pyshorteners.Shortener()
    print("Shortened URL : " + s.tinyurl.short(url))

shortenurl(url)
