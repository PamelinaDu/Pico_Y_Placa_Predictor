# -*- coding: utf-8 -*-
"""
Created on Thu May  6 23:11:10 2021

@author: USER
"""
import classes.license_plate as cl
import pytest

license_plate = cl.License_Plate("ABC-1234")


@pytest.mark.parametrize(
    "date_str, time_str, expected",
    [
        ("3-5-2021", "9:00", False),
        ("4-5-2021", "16:20", True),
        ("8-5-2021", "3:30", False)
    ]
)
def test_is_in_pico_y_placa_multi(date_str, time_str, expected):
    assert license_plate.is_in_pico_y_placa(date_str, time_str) == expected
