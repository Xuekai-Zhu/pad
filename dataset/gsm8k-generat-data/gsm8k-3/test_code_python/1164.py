def solution():
    """Hayden has a tank with a small hole in the bottom. The tank starts with 40 gallons of water. It loses 2 gallons of water per hour. Hayden does not add any water for the first two hours. He adds 1 gallon of water to the tank in hour three. He adds three gallons of water to the tank in the fourth hour. How much water is left in the tank at the end of the fourth hour?"""
    # Define the initial amount of water and the rate of water loss
    initial_water = 40
    water_loss_rate = 2

    # Calculate the amount of water remaining after 2 hours without adding water
    water_remaining = initial_water - (water_loss_rate * 2)

    # Add 1 gallon of water in the third hour
    water_remaining += 1

    # Add 3 gallons of water in the fourth hour
    water_remaining += 3

    # Display the amount of water remaining
    result = water_remaining
    return result

print(solution())