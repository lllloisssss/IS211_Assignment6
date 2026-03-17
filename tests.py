# tests.py
# Lois Arthur
# IS211 Assignment 6

from conversions import *


def testCelsiusToKelvin():
    print("Testing Celsius to Kelvin")

    assert convertCelsiusToKelvin(0) == 273.15
    print("0C to Kelvin passed")

    assert convertCelsiusToKelvin(100) == 373.15
    print("100C to Kelvin passed")

    assert convertCelsiusToKelvin(300) == 573.15
    print("300C to Kelvin passed")

    assert convertCelsiusToKelvin(-273.15) == 0
    print("-273.15C to Kelvin passed")

    assert convertCelsiusToKelvin(25) == 298.15
    print("25C to Kelvin passed")


def testCelsiusToFahrenheit():
    print("Testing Celsius to Fahrenheit")

    assert convertCelsiusToFahrenheit(0) == 32
    print("0C to Fahrenheit passed")

    assert convertCelsiusToFahrenheit(100) == 212
    print("100C to Fahrenheit passed")

    assert convertCelsiusToFahrenheit(300) == 572
    print("300C to Fahrenheit passed")

    assert convertCelsiusToFahrenheit(-40) == -40
    print("-40C to Fahrenheit passed")

    assert convertCelsiusToFahrenheit(25) == 77
    print("25C to Fahrenheit passed")


def testFahrenheitToCelsius():
    print("Testing Fahrenheit to Celsius")

    assert convertFahrenheitToCelsius(32) == 0
    print("32F to Celsius passed")

    assert convertFahrenheitToCelsius(212) == 100
    print("212F to Celsius passed")

    assert convertFahrenheitToCelsius(77) == 25
    print("77F to Celsius passed")

    assert convertFahrenheitToCelsius(-40) == -40
    print("-40F to Celsius passed")

    assert convertFahrenheitToCelsius(50) == 10
    print("50F to Celsius passed")


def testFahrenheitToKelvin():
    print("Testing Fahrenheit to Kelvin")

    assert convertFahrenheitToKelvin(32) == 273.15
    print("32F to Kelvin passed")

    assert convertFahrenheitToKelvin(212) == 373.15
    print("212F to Kelvin passed")

    assert convertFahrenheitToKelvin(77) == 298.15
    print("77F to Kelvin passed")

    assert convertFahrenheitToKelvin(-40) == 233.15
    print("-40F to Kelvin passed")

    assert convertFahrenheitToKelvin(50) == 283.15
    print("50F to Kelvin passed")


def testKelvinToCelsius():
    print("Testing Kelvin to Celsius")

    assert convertKelvinToCelsius(273.15) == 0
    print("273.15K to Celsius passed")

    assert convertKelvinToCelsius(373.15) == 100
    print("373.15K to Celsius passed")

    assert convertKelvinToCelsius(298.15) == 25
    print("298.15K to Celsius passed")

    assert convertKelvinToCelsius(233.15) == -40
    print("233.15K to Celsius passed")

    assert convertKelvinToCelsius(283.15) == 10
    print("283.15K to Celsius passed")


def testKelvinToFahrenheit():
    print("Testing Kelvin to Fahrenheit")

    assert convertKelvinToFahrenheit(273.15) == 32
    print("273.15K to Fahrenheit passed")

    assert convertKelvinToFahrenheit(373.15) == 212
    print("373.15K to Fahrenheit passed")

    assert convertKelvinToFahrenheit(298.15) == 77
    print("298.15K to Fahrenheit passed")

    assert convertKelvinToFahrenheit(233.15) == -40
    print("233.15K to Fahrenheit passed")

    assert convertKelvinToFahrenheit(283.15) == 50
    print("283.15K to Fahrenheit passed")


testCelsiusToKelvin()
testCelsiusToFahrenheit()
testFahrenheitToCelsius()
testFahrenheitToKelvin()
testKelvinToCelsius()
testKelvinToFahrenheit()
