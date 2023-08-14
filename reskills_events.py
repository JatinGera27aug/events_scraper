from bs4 import BeautifulSoup
import requests
from datetime import date

# extracting today's date
today = date.today()
date_today = today.strftime("%Y-%m-%d")
print(date_today)
def scrape():

    site_link = "https://reskilll.com/allevents"

    data = requests.get(site_link)
    data = BeautifulSoup(data.text, "html.parser")
    return data

page=scrape()


events_listed = []
try:
    events = page.find_all(class_="eventtopic eventName pb-2")
    for text in events:
        get_event = text.get_text()
        
        events_listed.append(get_event)
except:
    message = f"not found !"
    print(message)

#print(events_listed)

events_name=[]
for i in range(len(events_listed)):
    for j in events_listed[i]:
        if j=='\n' or j==' ':
            #event_name = events_listed[i].replace('                                    ','').replace('\n','').replace('                               ','')
            event_name = (events_listed[i].replace('\n','')).strip()
            events_name.append(event_name)
            break
        
#print(events_name)


#events_dates

events_date_listed = []
try:
    events = page.find_all(class_="eventdate ps-4")
    for text in events:
        get_event_dates = text.get_text()
        
        events_date_listed.append(get_event_dates)
except:
    message = f"not found !"
    print(message)

#print(type(events_date_listed[1]))


month_list_num=['01','02','03','04','05','06','07','08','09','10','11','12']
month_list_alpha=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
events_date=[]
live_events_date=[]
for i in range(len(events_date_listed)):
    for j in events_date_listed[i]:
        if j=='\n' or j==' ':
            #event_name = events_listed[i].replace('                                    ','').replace('\n','').replace('                               ','')
            event_date = (((events_date_listed[i].replace('\n','')).strip()).replace(' ','-'))
            a=event_date[0:3]
            #print("a is",a)
            for k in range(len(month_list_alpha)):
                if event_date[0:3]==month_list_alpha[k]:
                    event_dates_num=event_date[0:3].replace(a,month_list_num[k])+event_date[3:]
                    #print(event_dates_num)
            event_date_formatted = event_dates_num[-4:]+'-'+event_dates_num[:5]
            events_date.append(event_date_formatted)
            break

print(events_date)
count_live=0
for i in range(len(events_date)):
        if events_date[i]>=date_today:
            live_events_date.append((events_date)[i])
            count_live+=1
#print(live_events_date)

#extracting link of events

events_link = []
try:
    events = page.find_all('a', class_="text-decoration-none registerevent")    
    
    Counter=0
    for ev in events:
        #print(ev.get('href'))
        events_link.append(ev.get('href'))
        Counter+=1
        if Counter==count_live:
            break
        else:
            pass
except:
    message = f"not found !"
    print(message)
#print(events_link)

#final list
event_full_detail = []
for i in range(count_live):
    add_both = events_name[i]+' on '+live_events_date[i]+ '  ------LINK IS-----> '+events_link[i]
    event_full_detail.append(add_both)
#print(event_full_detail)
#above working fine

for event_full_info in event_full_detail:
    print(event_full_info)
    print()
