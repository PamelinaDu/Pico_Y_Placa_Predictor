#!/usr/bin/env python
# coding: utf-8
"""
Created on Thu May  6  2021

@author: Pamela Dután
"""
import functions.validation_functions as vf

def input_license():
    license_plate_str = input ("Entry your license plate number using the format ABC-0123: ")
    while not vf.is_valid_license(license_plate_str):
        print("Invalid license.")
        license_plate_str = input ("Please entry a license using the format ABC-0123: ")
    return license_plate_str


def input_date():
    date_str = input ("Entry a date in format dd-mm-yyyy: ")
    while not vf.is_valid_date(date_str):
        date_str = input ("Please entry a date using this format dd-mm-yyyy: ")
    return date_str


def input_time():
    time_str = input ("Entry a time in format hh:mm :  ")
    while not vf.is_valid_time(time_str):
        time_str = input ("Please entry a time in format hh:mm :  ")
    return time_str

