def solution():
    """Jacob's water tank can hold up to 50 liters of water. Jacob collects water from the river and rain to fill his water tank.
    He can collect 800 milliliters of water from the rain and 1700 milliliters of water from the river every day. How many days does Jacob need to fill up his water tank?"""
    # Convert the collected water from milliliters to liters
    rain_water = 800 / 1000
    river_water = 1700 / 1000

    # Calculate the daily amount of water collected
    daily_water = rain_water + river_water

    # Calculate the number of days required to fill up the tank
    days_to_fill = 50 / daily_water

    # Display the number of days required
    result = days_to_fill
    return result

print(solution())