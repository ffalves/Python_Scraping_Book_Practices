from urllib.request import urlopen
from bs4 import BeautifulSoup #must have pip install beautifulsoup4
from urllib.error import HTTPError, URLError # to tackle with errors

# Initial practices
html = urlopen( 'http://www.pythonscraping.com/pages/page1.html' )

# With .read() method
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)

# Without .read() method; and examples has the same outputs regardeless path
bs = BeautifulSoup(html, 'html.parser')
print(bs.h1)
print(bs.html.body.h1)
print(bs.body.h1)
print(bs.html.h1)

# Parser argument: the next options are better for working with poorly formatted HTML
bs = BeautifulSoup(html.read(), 'lxml') #must have pip install lxml
print(bs.h1)

bs = BeautifulSoup(html.read(), 'html5lib') #must have pip install html5lib
print(bs.html.h1)

# Dealing with 2 errors possibilities during scraping
# 1. if the page isn't found or the server isn't found
try:
    html = urlopen( 'http://www.pythonscraping.com/pages/page1.html' )
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It worked, honey!')

# 2. to make sure that a tag actually exists

try:
    badContent = bs.nonExistingTag.anotherTag
except AttributeError as e:
    print('Tag was not found!')
else:
    if badContent == None:
        print ('Tag was not found!')
    else:
        print(badContent)

# We can working with a function to do all these jobs, called getTitle()
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'lxml')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

# Here we cant test the function getTitle()
title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found!')
else:
    print(title)




