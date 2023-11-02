def solution():
    """A water tank has a capacity of 4000 gallons. Mack connects a pipe to the tank that fills the tank with water at the rate of 10 gallons per hour. How long will it take to fill the tank to 3/4 of its capacity?"""
    # Define the capacity of the water tank and the filling rate
    capacity = 4000
    filling_rate = 10

    # Calculate the amount of water needed to fill the tank to 3/4 of its capacity
    water_needed = 0.75 * capacity

    # Calculate the time it will take to fill the tank to 3/4 of its capacity
    time = water_needed / filling_rate

    # Display the time
    result = time
    return result

print(solution())