import sys
import datetime


"""
The problem statement is find the days on which each base_number has more trips.
use the dataset uber for this example.
"""

def mapper():
    for line in sys.stdin:
        line=line.strip()
        line = line.split(",")
        base_number = line[0]
        date_current = line[1]
        trips = line[3]
        day=""
        month=""
        week_day=""
        date_current = date_current.split("/")

# Converting the date format given in the file to the datetime object to easily
# retriev the week_day
# making key as
# key,value:
# base_number date, No. of trips

        try:
            if len(date_current[0]) < 2:
                day = "0" + date_current[0]
            else:
                day = date_current[0]
            if len(date_current[1]) < 2:
                month = "0" + date_current[1]
            else:
                month = date_current[1]
            date_current = day + month + date_current[2]
            date_current = datetime.datetime.strptime(date_current,"%m%d%Y").date()
            week_day =date_current.strftime("%A")
        except IndexError:
            continue
        except:
            week_day="error"

        key=base_number+" "+week_day
        print(key,trips,sep=",")

mapper()
