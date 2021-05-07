# -*- coding: utf-8 -*-
"""
Created on Thu May  6 23:48:05 2021

@author: Pamela Dután
"""
import pytest
import functions.validation_functions as vf
import calendar


def test_is_valid_license():
    assert vf.is_valid_license("ABC-1243") == True


@pytest.mark.parametrize(
    "license_plate_str, expected",
    [
        ("ABC-1234", True),
        ("AWB-012", True),
        ("IT-0989", True),
        ("abc-1234", True),
        ("AbC-1234", True)
    ]
)
def test_is_valid_license_multi(license_plate_str, expected):
    assert vf.is_valid_license(license_plate_str) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("15-11-2011", True),
        ("5-5-2010", True),
        ("35-11-2012", False),
        ("25 de noviembre del 2003", False),
        ("15/11/2010", False),
        ("23.05.2012", False)
    ]
)
def test_is_valid_date_multi(date_str, expected):
    assert vf.is_valid_date(date_str) == expected


@pytest.mark.parametrize(
    "time_str, expected",
    [
        ("15:23", True),
        ("3:50", True),
        ("3:80", False),
        ("3 horas con 20 minutos", False),
        ("24:00", False),
        ("12:12:12", False)
    ]
)
def test_is_valid_time_multi(time_str, expected):
    assert vf.is_valid_time(time_str) == expected


@pytest.mark.parametrize(
    "time_str, expected",
    [
        ("07:30", True),
        ("09:00", True),
        ("16:00", True),
        ("19:30", True),
        ("12:30", False),
        ("20:00", False)
    ]
)
def test_is_pico_y_placa_hour_multi(time_str, expected):
    assert vf.is_pico_y_placa_hour(time_str) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("7-05-2021", calendar.day_name[4]),
        ("6-05-2021", calendar.day_name[3])
    ]
)
def test_conversion_to_day_multi(date_str, expected):
    assert vf.conversion_to_day(date_str) == expected


@pytest.mark.parametrize(
    "number_part, date_str, expected",
    [
        ("351", "3-5-2021", True),
        ("4552", "3-5-2021", True),
        ("3456", "3-5-2021", False),
        ("2340", "7-5-2021", True)
    ]
)
def test_is_pico_y_placa_day_multi(number_part, date_str, expected):
    assert vf.is_pico_y_placa_day(number_part, date_str) == expected
