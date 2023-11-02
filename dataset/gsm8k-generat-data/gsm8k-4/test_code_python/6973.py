def solution():
    """A water tank has a capacity of 4000 gallons. Mack connects a pipe to the tank that fills the tank with water at the rate of 10 gallons per hour. How long will it take to fill the tank to 3/4 of its capacity?"""
    # Define the total capacity of the water tank
    total_capacity = 4000

    # Calculate the capacity Mack wants to fill
    fill_capacity = total_capacity * 0.75

    # Calculate the rate of water flow and the time it will take to fill the desired capacity
    rate = 10  # gallons per hour
    time = fill_capacity / rate

    # Return the time in hours
    result = time
    return result

print(solution())