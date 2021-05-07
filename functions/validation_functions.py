# -*- coding: utf-8 -*-
"""
Created on Thu May  6 01:03:43 2021

@author: Pamela Dután
"""
import datetime 
import calendar

def is_valid_license(license_plate_str): 
    if not len(license_plate_str) in range(7,9):  #Valid string size
        return False
    else:
        license_groups = license_plate_str.split("-")  
        if len(license_groups) != 2:  #Valid the license format 
            return False
        
        letters = license_groups[0]        
        if not letters.isalpha():     #Valid letters group 
            return False
        
        numbers = license_groups[1]  #Valid numbers group
        if not numbers.isnumeric():
            return False
    return True


def is_valid_date(date_str): 
    try:
        datetime.datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        return False
    return True
        
def is_valid_time(time_str):
    try:
        datetime.datetime.strptime(time_str, '%H:%M').time()  
    except ValueError:
        return False
    return True

def is_pico_y_placa_hour(time_str):
    time_object = datetime.datetime.strptime(time_str, '%H:%M').time()
    hour_limits = {
    "morning": ["7:00" , "9:30"],
    "evening": ["16:00" , "19:30"]
    }

    for key in hour_limits:
        intervals = hour_limits[key]
        limit_time_min = datetime.datetime.strptime(intervals[0], '%H:%M').time()
        limit_time_max = datetime.datetime.strptime(intervals[1], '%H:%M').time()
    
        if not  limit_time_min <= time_object <= limit_time_max :
            return False
    return True

def conversion_to_day(date_str):
    date_object = datetime.datetime.strptime(date_str, "%d-%m-%Y") 
    day_object = calendar.day_name[date_object.weekday()] 
    return day_object

def is_pico_y_placa_day(number_part, date_str):
    day_object = conversion_to_day(date_str)
    days_not_valid = [calendar.day_name[5], calendar.day_name[6]]
    for day in days_not_valid:
      if day_object == day:
          return False 
    
    pico_y_placa_days = {   
       calendar.day_name[0]:[1,2],  #Monday
       calendar.day_name[1]:[3,4],  #Tuesday
       calendar.day_name[2]:[5,6],
       calendar.day_name[3]:[7,8],
       calendar.day_name[4]:[9,0]
    }
    last_digit = int(number_part[-1])
    
    for key in pico_y_placa_days:
        last_numbers = pico_y_placa_days[key]
        for digit in last_numbers:
            if not digit == last_digit:
                return False
    return True
    



