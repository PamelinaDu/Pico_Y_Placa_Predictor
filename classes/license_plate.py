# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:47:59 2021

@author: USER
"""
import functions.validation_functions as vfs

class License_Plate: 
    def __init__(self, license_plate_str):
        self.asignation_part_values(license_plate_str)
        self.asignation_license_type(self.letter_part)
        
    def asignation_part_values(self, license_plate_str):
        license_groups = license_plate_str.split("-")
        self.letter_part = license_groups[0]
        self.number_part = license_groups[1]
        
    def asignation_license_type(self, letter_part):
        license_type = ""
        if len(letter_part) == 2:
            if letter_part=="IT":
                license_type = "International Organization license "
            else:
                license_type = "Diplomatic licence"
        else:
            if letter_part[1] == "W":
                license_type = "Police license"
            elif letter_part [1] =="E":
                license_type = "Goverment license"
            elif letter_part [1]=="X":
                license_type = "Official use license"
            elif letter_part =="M" or letter_part =="S" :
                license_type = "Decentralized autonomous government license"
            else:
                license_type = "Private or commercial license"
        self.license_type = license_type
        
    def is_in_pico_y_placa(self, date_str, time_str):
        if not self.license_type == "Private or commercial vehicle license":
            if vfs.is_pico_y_placa_day(self.number_part, date_str):
                if vfs.is_pico_y_placa_hour(time_str):
                    return True
        return False