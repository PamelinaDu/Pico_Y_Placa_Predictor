#!/usr/bin/env python
# coding: utf-8

import datetime 


def is_valid_license(license_number_str): 
    if not len(license_number_str) in range(7,9):  #Valid string size
        return False
    else:
        license_groups = license_number_str.split("-")  
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
        date_object = datetime.datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError as d:
        print('ValueError:', d)
        return False
    return True
        
def is_valid_time(time_str):
    try:
        time_object = datetime.datetime.strptime(time_str, '%H:%M').time()  
    except ValueError as d:
        print('ValueError:', d)
        return False
    return True


def input_license(license):
    license_number_str = input ("Entry your license plate number using the format ABC-0123: ")
    while not is_valid_license(license_number_str):
        print("Invalid license.")
        license_number_str = input ("Please use the format ABC-0123: ")
    return license_number_str


def input_date(date):
    date_str = input ("Entry a date in format dd-mm-yyyy: ")
    while not is_valid_date(date_str):
        date_str = input ("Please entry a date using this format dd-mm-yyyy: ")
    return date_str


def input_time(time):
    time_str = input ("Entry a time in format hh:mm :  ")
    while not is_valid_time(time_str):
        time_str = input ("Please entry a time in format hh:mm :  ")
    return time_str

