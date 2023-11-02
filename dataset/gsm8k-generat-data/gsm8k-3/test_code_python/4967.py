def solution():
    """A company has a tank that is already filled at a maximum capacity of 350,000 gallons of water. One day the tank starts losing 32,000 gallons/hour for 5 hours, after that time the company repaired the tank but it wasn't enough because the tank was still losing 10,000 gallons/hour. It stayed like that for 10 hours. In the second attempt, they managed to repair the tank and started filling it with 40,000 gallons/hour. After 3 hours, how many gallons are missing for the tank to be at maximum capacity again?"""
    # Define the maximum capacity of the tank
    MAX_CAPACITY = 350000

    # Calculate the amount of water lost in the first 5 hours
    water_lost_1 = 32000 * 5

    # Calculate the amount of water lost in the next 10 hours
    water_lost_2 = 10000 * 10

    # Calculate the amount of time it took to repair the tank
    repair_time = 5 + 10

    # Calculate the amount of water that was missing when they started filling the tank again
    missing_water = MAX_CAPACITY - (water_lost_1 + water_lost_2)

    # Calculate the amount of water filled in the second attempt
    filled_water = 40000 * 3

    # Calculate the final amount of water in the tank
    final_water = MAX_CAPACITY - (missing_water - filled_water)

    # Calculate the amount of water missing to reach maximum capacity
    missing_capacity = MAX_CAPACITY - final_water

    # Display the amount of water missing
    result = missing_capacity
    return result

print(solution())