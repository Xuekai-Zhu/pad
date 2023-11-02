def solution():
    """A tank can hold 100 liters of water. At the beginning of the rainy season, the tank is 2/5 filled with water. On the first day of the rainy season, the tank collected 15 liters of water. On the second day, 5 liters more water was collected than on the first day. On the third day, the tank was already filled. How many liters of water were collected on the third day?"""
    # Define the total capacity of the tank and the initial amount of water
    TOTAL_CAPACITY = 100
    initial_water = TOTAL_CAPACITY * 2 / 5

    # Calculate the amount of water collected on the first and second day
    water_collected_first_day = 15
    water_collected_second_day = water_collected_first_day + 5

    # Calculate the remaining capacity of the tank
    remaining_capacity = TOTAL_CAPACITY - initial_water - water_collected_first_day - water_collected_second_day

    # Calculate the amount of water collected on the third day
    water_collected_third_day = remaining_capacity

    result = water_collected_third_day
    return result

print(solution())