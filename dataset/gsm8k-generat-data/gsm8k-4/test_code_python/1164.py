def solution():
    """Hayden has a tank with a small hole in the bottom. The tank starts with 40 gallons of water. It loses 2 gallons of water per hour. Hayden does not add any water for the first two hours. He adds 1 gallon of water to the tank in hour three. He adds three gallons of water to the tank in the fourth hour. How much water is left in the tank at the end of the fourth hour?"""
    # Define the initial amount of water in the tank
    initial_water = 40

    # Calculate the amount of water left after two hours
    water_after_2_hours = initial_water - 2 * 2

    # Add 1 gallon of water in hour three
    water_after_3_hours = water_after_2_hours + 1

    # Add 3 gallons of water in hour four
    water_after_4_hours = water_after_3_hours + 3

    # Return the amount of water in the tank at the end of the fourth hour
    result = water_after_4_hours
    return result

print(solution())