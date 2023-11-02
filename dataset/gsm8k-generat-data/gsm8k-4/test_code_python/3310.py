def solution():
    """Aubriella is pouring water into a 50-gallon fish tank at the rate of 1 gallon every 20 seconds. How many more gallons will she have to pour into the tank to fill the tank if she poured water into the fish tank for 6 minutes?"""
    # Define the rate of pouring water in gallons per second
    rate = 1 / 20

    # Define the time in seconds that water has been poured into the tank
    time = 6 * 60

    # Calculate the total amount of water poured into the tank so far
    total_water = rate * time

    # Calculate the amount of water needed to fill the tank
    remaining_water = 50 - total_water

    # Return the result
    result = remaining_water
    return result

print(solution())