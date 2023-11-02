def solution():
    """Aubriella is pouring water into a 50-gallon fish tank at the rate of 1 gallon every 20 seconds. How many more gallons will she have to pour into the tank to fill the tank if she poured water into the fish tank for 6 minutes?"""
    # Define the rate of pouring in gallons per second
    GALLONS_PER_SECOND = 1 / 20
    
    # Define the number of seconds in 6 minutes
    TIME_IN_SECONDS = 6 * 60

    # Calculate the total amount of water poured into the tank in 6 minutes
    total_water_poured = GALLONS_PER_SECOND * TIME_IN_SECONDS

    # Calculate the remaining amount of water needed to fill the tank
    remaining_water_needed = 50 - total_water_poured

    # Display the remaining amount of water needed
    result = remaining_water_needed
    return result

print(solution())