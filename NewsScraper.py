from bs4 import BeautifulSoup
import requests

# web scraper for news on inquirer
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"} # user agent for to get access
def InquirerMain():
    html_text = requests.get("https://www.inquirer.net/", headers=headers).text # convert page to text
    soup = BeautifulSoup(html_text, "lxml")
    tags = soup.find_all("div", class_="flx-l-head") # find text with that class

    print("front news")

    ntags = str(tags)
    first = ntags.replace("</div>,", "") # remove text
    second = first.replace('<div class="flx-l-head">', '') # remove text
    print(second[1:-7]) # remove other tags

def InquirerNews():
    html_text = requests.get("https://newsinfo.inquirer.net/", headers=headers).text # convert page to text
    soup = BeautifulSoup(html_text, "lxml")
    tags = soup.find_all("h1") # find text with that class

    print("current news")

    ntags = str(tags)
    

    for ch in ["<h1>","</h1>","<a>","</a>","<a href=","[","]"]:  # remove tags in text
        if ch in ntags:
            ntags = ntags.replace(ch,"")

    nlist = list(ntags.split(","))
    print(*nlist, sep = "\n") # print list wiht newline seperator

def InquirerBusiness():
    html_text = requests.get("https://business.inquirer.net/", headers=headers).text # convert page to text
    soup = BeautifulSoup(html_text, "lxml")
    tags = soup.find_all("h1") # find text with that class

    print("current business news")

    ntags = str(tags)
    

    for ch in ["<h1>","</h1>","<a>","</a>","<a href=","[","]",'<h1 style="color:#fff;">']:  # remove tags in text
        if ch in ntags:
            ntags = ntags.replace(ch,"")

    nlist = list(ntags.split(","))
    print(*nlist, sep = "\n") # print list wiht newline seperator

def InquirerStockExchange():
    html_text = requests.get("https://business.inquirer.net/category/stock-market-table", headers=headers).text # convert page to text
    soup = BeautifulSoup(html_text, "lxml")
    tags = soup.find_all("h2") # find text with that class

    print("current stock exchange news page 1")

    ntags = str(tags)
    

    for ch in ["<h2>","</h2>","<a>","</a>","<a href=","[","]",]:  # remove tags in text
        if ch in ntags:
            ntags = ntags.replace(ch,"")

    nlist = list(ntags.split(","))
    print(*nlist, sep = "\n") # print list wiht newline seperator

    html_text = requests.get("https://business.inquirer.net/category/stock-market-table/page/2", headers=headers).text # convert page to text
    soup = BeautifulSoup(html_text, "lxml")
    tags = soup.find_all("h2") # find text with that class

    print("current stock exchange news page 2")

    ntags = str(tags)
    

    for ch in ["<h2>","</h2>","<a>","</a>","<a href=","[","]",]:  # remove tags in text
        if ch in ntags:
            ntags = ntags.replace(ch,"")

    nlist = list(ntags.split(","))
    print(*nlist, sep = "\n") # print list wiht newline seperator

#InquirerBusiness()
#InquirerNews()
#InquirerMain()
#InquirerStockExchange()