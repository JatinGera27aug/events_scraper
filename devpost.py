from bs4 import BeautifulSoup
import requests
import urllib2
soup = BeautifulSoup(urllib2.urlopen("https://devpost.com/hackathons"))
result = soup.find_all("div", {"class":"content"})
for res in result:
    print(res.text)










# def scrape():

#     site_link = "https://devpost.com/hackathons"

#     data = requests.get(site_link)
#     data = BeautifulSoup(data.text, "html.parser")
#     return data

# page=scrape()


# events_listed_open = []
# count=0
# try:
#     events = page.find_all("div",{"class":"content"})
#     for text in events:
#         print(text.text)
#         # print(get_event_open)
#         #events_listed_open.append(get_event_open)
#         count+=1
#         if count==10:
#             break
#     print(events)
# except:
#     message = f"not found !"
#     print(message)

# print(events_listed_open)