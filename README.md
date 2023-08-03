# Weather-Data-Scrap-WWDS

## Description
The Weather Data Scrap Application is a Python-based web scraping tool that extracts weather data from the popular website timeanddate.com. The application utilizes the BeautifulSoup library to parse the website's HTML content and retrieve valuable weather information for 140 most popular cities.

## Features
Easy-to-Use: The application provides a user-friendly interface, making it simple for users to specify the location and date range for weather data extraction.

Accurate Data: By leveraging timeanddate.com's reliable weather data, the application ensures that users receive accurate and up-to-date weather information.

Data Export: Extracted weather data is stored in an Excel file, allowing users to access and analyze the information for future reference.

## Functionalities:
### worldWideReport(): 
This Generates the world wide weather reports in list format.

### saveToExcel(): 
This Generates the world wide weather reports in an excel sheet.

## Example

    from TimeanddateScrapper.worldweather import Weather
    w = Weather()
    print(w.worldWideReport())
    w.saveToExcel()
