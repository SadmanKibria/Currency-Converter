import requests
from bs4 import BeautifulSoup
import click

# Define the URL of the website with exchange rates
EXCHANGE_RATE_URL = "https://www.example.com/exchange-rates"

# Function to fetch exchange rates from the website
def fetch_exchange_rates():
    try:
        response = requests.get(EXCHANGE_RATE_URL)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Parse the exchange rates from the website here
        # Example: exchange_rates = {"EUR": 0.85, "GBP": 0.75, "BDT": 100.0}
        exchange_rates = {
            "EUR": 0.85,
            "GBP": 0.75,
            "BDT": 100.0
        }
        
        return exchange_rates
    except Exception as e:
        print("Error fetching exchange rates:", str(e))
        return None

# Function to perform currency conversion
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return None

    rate_from = exchange_rates[from_currency]
    rate_to = exchange_rates[to_currency]

    converted_amount = amount * (rate_to / rate_from)
    return converted_amount

@click.command()
@click.option("--amount", type=float, help="Amount to convert")
@click.option("--from-currency", type=str, help="Source currency")
@click.option("--to-currency", type=str, help="Target currency")
def main(amount, from_currency, to_currency):
    if not all([amount, from_currency, to_currency]):
        click.echo("Please provide amount, source currency, and target currency.")
        return

    exchange_rates = fetch_exchange_rates()

    if exchange_rates:
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        
        if from_currency == to_currency:
            click.echo("Source and target currencies are the same. No conversion needed.")
        else:
            converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
            if converted_amount is not None:
                click.echo(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
            else:
                click.echo("Invalid currency codes. Please check your input.")
    else:
        click.echo("Failed to fetch exchange rates. Please try again later.")

if __name__ == "__main__":
    main()
