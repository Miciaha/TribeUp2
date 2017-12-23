import untangle
import time
import datetime
from urllib.request import urlopen
from .models import Event,BuildInfo
import sqlite3



#Use current date to keep track of how far to update events
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
current_year = datetime.datetime.now().year


def build_check():
    #The purpose of this method is to reduce data redundancy 
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    cmd = cursor.execute('select build_year from events_buildinfo where build_year=' + str(current_year) + ' and build_month=' + str(current_month))
    build_year_fetch = cmd.fetchone()

    try:
        build_year = build_year_fetch[0]
        print(build_year)
    except Exception:
        build_model() 





def build_model():
    #This method is called after ensuring that the database doesn't have anything stored for the current month
    month = month_to_string(current_month)

    my_url = 'http://calendar.fsu.edu/search/events.xml'
    xml = untangle.parse(my_url)

    new_build = BuildInfo(build_year=current_year, build_month=current_month, build_month_string=month)
    new_build.save()

    for item in xml.rss.channel.item:
    #Prettifying date
        title = item.title.cdata
        prettyDate = title.split(': ')[0]
        day_month = prettyDate.split(', ')[0]
        event_month = day_month.split(' ')[0]
        event_day = day_month.split(' ')[1]
        year = int(prettyDate.split(', ')[1])

        if event_month == month and current_year == year:
            evt_title = title.split(': ')[1]
            evt_link = item.link.cdata
            description = item.description.cdata


         #"try/catch" for category; not all items have a category attribute
            try:
                category = item.category.cdata
                #Exception passing for unique values. If there is a repeat, we'll skip over it and continue searching this month
                try:
                    new_event = Event(event_name=evt_title, event_month=event_month, event_day=event_day, event_description=description, event_type=category, event_link=evt_link)
                    new_event.save()
                except Exception:
                    pass


            except:
                category = "General"
                try:
                    new_event = Event(event_name=evt_title, event_month=event_month, event_day=event_day, event_description=description, event_type=category, event_link=evt_link)
                    new_event.save()
                except Exception:
                    pass


def month_to_string(month_int):
    #This is needed to match current month with data pulled from XML form
    converter = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    return converter.get(month_int, "Invalid Number")
