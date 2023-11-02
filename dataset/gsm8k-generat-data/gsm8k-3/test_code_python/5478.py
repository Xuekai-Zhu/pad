def solution():
    """A tank can hold 100 liters of water. At the beginning of the rainy season, the tank is 2/5 filled with water. On the first day of the rainy season, the tank collected 15 liters of water. On the second day, 5 liters more water was collected than on the first day. On the third day, the tank was already filled. How many liters of water were collected on the third day?"""
    # Define the capacity of the tank
    TANK_CAPACITY = 100

    # Calculate the amount of water already in the tank
    initial_water = TANK_CAPACITY * 2/5

    # Calculate the amount of water collected on the first day
    day1_water = 15

    # Calculate the amount of water collected on the second day
    day2_water = day1_water + 5

    # Calculate the amount of water needed to fill the tank
    remaining_water = TANK_CAPACITY - initial_water - day1_water - day2_water

    # The remaining water on the third day is equal to the needed water to fill the tank
    day3_water = remaining_water

    # Display the amount of water collected on the third day
    result = day3_water
    return result

print(solution())