from datetime import datetime, timedelta


#1
def subtract_five_days():
    current_date = datetime.now()
    new_date = current_date - timedelta(days=5)
    return new_date.strftime("%Y-%m-%d")

#print(subtract_five_days())


#2
def get_dates():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    
    return yesterday.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d"), tomorrow.strftime("%Y-%m-%d")

yesterday, today, tomorrow = get_dates()

#print("Yesterday:", yesterday)
#print("Today:", today)
#print("Tomorrow:", tomorrow)


#3
def get_datetime_without_microseconds():
    current_datetime = datetime.now().replace(microsecond=0)
    return current_datetime

#print(get_datetime_without_microseconds())


#4
def date_difference_in_seconds():
    format_str = "%Y-%m-%d %H:%M:%S"
    date1 = input("dt1: ")
    date2 = input("dt2: ")
    
    dt1 = datetime.strptime(date1, format_str)
    dt2 = datetime.strptime(date2, format_str)
    
    return abs(int((dt2 - dt1).total_seconds()))

#print(date_difference_in_seconds())
