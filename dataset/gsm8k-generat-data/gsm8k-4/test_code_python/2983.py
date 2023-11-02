def solution():
    """Jacob's water tank can hold up to 50 liters of water. Jacob collects water from the river and rain to fill his water tank. He can collect 800 milliliters of water from the rain and 1700 milliliters of water from the river every day. How many days does Jacob need to fill up his water tank?"""
    # Define the maximum capacity of the water tank and the daily collection rates
    TANK_CAPACITY = 50
    RAIN_COLLECTION = 800
    RIVER_COLLECTION = 1700

    # Initialize the total collected water and the number of days
    total_water = 0
    days = 0

    # Keep collecting water until the tank is full
    while total_water < TANK_CAPACITY:
        # Calculate the daily collection
        daily_collection = RAIN_COLLECTION + RIVER_COLLECTION

        # Add the daily collection to the total
        total_water += daily_collection / 1000

        # Increment the number of days
        days += 1
        
    # Display the number of days it took to fill up the water tank
    result = days
    return result

print(solution())