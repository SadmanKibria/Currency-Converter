# Real-Time Currency Converter

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Dependencies](#dependencies)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Introduction
This Python program allows you to perform real-time currency conversion. It fetches the latest exchange rates from a reliable source and provides a user-friendly command-line interface for converting between different currencies.

## Features

- Real-time currency conversion using the latest exchange rates.
- Support for multiple currencies, including Euro (EUR), British Pound (GBP), and Bangladeshi Taka (BDT).
- User-friendly command-line interface.
- Handles input validation to prevent errors.
- Easy-to-read and well-commented Python code.

## Dependencies

To run this program, you need to have the following dependencies installed:

- [Requests](https://docs.python-requests.org/en/master/): A Python library for making HTTP requests.
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/): A Python library for web scraping.
- [Click](https://click.palletsprojects.com/en/8.x/): A Python library for creating command-line interfaces.

You can install these dependencies using pip:

`pip install requests beautifulsoup4 click`

## Getting Started

1. Clone this repository to your local machine:
`git clone https://github.com/your-username/currency-converter.git`

2. Navigate to the project directory:
`cd currency-converter`

3. Run the program by executing the following command:
`python currency_converter.py`

## Usage
To use the currency converter, follow these steps:

1. Run the program as mentioned in the "Getting Started" section.
2. Provide the following information:
`--amount`: The amount you want to convert.
`--from-currency`: The source currency code (e.g., USD, EUR, BDT).
`--to-currency`: The target currency code (e.g., USD, EUR, BDT).
3. Press Enter to perform the conversion.
4. The program will display the converted amount.

**Note:** Ensure that you enter valid currency codes, and the source and target currencies are not the same.

## Project Structure

The project directory contains the following files:

`currency_converter.py`: The Python script for the currency converter.
`README.md`: This documentation file.

## Licence
This project is open-source and available under the [MIT License](LICENSE). 

Feel free to explore, use, and contribute to the Weather Dashboard. We hope it enhances your understanding of weather conditions and provides an enjoyable user experience.
