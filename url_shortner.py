import pyshorteners

url = input('Drop your Url to shorten:')


def shortenurl(url):
    s = pyshorteners.Shortener()
    print("Here is the shortened url :" , s.tinyurl.short(url))

shortenurl(url)