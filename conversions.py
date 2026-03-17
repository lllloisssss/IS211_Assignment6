# conversions.py
# Lois Arthur
# IS211 Assignment 6

# Convert Celsius to Kelvin
def convertCelsiusToKelvin(celsius):
    return celsius + 273.15


# Convert Celsius to Fahrenheit
def convertCelsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32


# Convert Fahrenheit to Celsius
def convertFahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


# Convert Fahrenheit to Kelvin
def convertFahrenheitToKelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15


# Convert Kelvin to Celsius
def convertKelvinToCelsius(kelvin):
    return kelvin - 273.15


# Convert Kelvin to Fahrenheit
def convertKelvinToFahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32
