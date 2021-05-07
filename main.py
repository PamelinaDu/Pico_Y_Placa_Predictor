# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:46:56 2021

@author: Pamela Dután
"""
import functions.input_functions as inf
from classes.license_plate import License_Plate

while True:
    license_plate_str = inf.input_license()
    date_str = inf.input_date()
    time_str = inf.input_time()

    license_plate = License_Plate(license_plate_str)

    if not license_plate.is_in_pico_y_placa(date_str, time_str):
        print("This car CAN be on the road")
        print("License Type: " + license_plate.license_type)
    else:
        print("This car CAN NOT be on the road")
        print("License Type: " + license_plate.license_type)