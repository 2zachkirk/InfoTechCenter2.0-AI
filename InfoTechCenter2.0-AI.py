import random
from time import sleep


# Function to get the current gas level randomly
def get_gas_level():
    gas_levels = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter", "Full Tank"]
    return random.choice(gas_levels)


# Function to get a random gas station
def get_gas_station():
    gas_stations = ["Shell", "Speedway", "7Eleven", "Marathon", "Circle-K", "Costco", "Meijer", "Valvoline"]
    return random.choice(gas_stations)


# Function to alert about gas level and nearest gas station if necessary
def gas_level_alert():
    # Generate random miles to gas stations for low and quarter tank levels
    miles_to_gas_stations_low = round(random.uniform(1, 25), 1)
    miles_to_gas_stations_quarter_tank = round(random.uniform(25.1, 50), 1)

    # Get the current gas level
    gas_level = get_gas_level()

    # Determine actions based on the gas level
    if gas_level == "Empty":
        print("*** WARNING - YOU ARE ON EMPTY ***")
        sleep(2.5)
        print("     *** Calling Triple AAA ***")
    elif gas_level == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print(f"The closest gas station is {get_gas_station()}, which is {miles_to_gas_stations_low} miles away.")
    elif gas_level == "Quarter Tank":
        print("Your gas tank is on a quarter tank, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print(
            f"The closest gas station is {get_gas_station()}, which is {miles_to_gas_stations_quarter_tank} miles away.")
    elif gas_level == "Half Tank":
        print("Your gas tank is half full which is plenty to get to your destination.")
    elif gas_level == "Three Quarter":
        print("Your gas tank is three quarters full.")
    else:
        print("Your gas tank is full. No need to refuel now! Have a safe journey!")


# Call the gas level alert function to check gas level and take necessary actions
gas_level_alert()
