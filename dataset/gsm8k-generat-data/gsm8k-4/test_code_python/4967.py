def solution():
    """A company has a tank that is already filled at a maximum capacity of 350,000 gallons of water. One day the tank starts losing 32,000 gallons/hour for 5 hours, after that time the company repaired the tank but it wasn't enough because the tank was still losing 10,000 gallons/hour. It stayed like that for 10 hours. In the second attempt, they managed to repair the tank and started filling it with 40,000 gallons/hour. After 3 hours, how many gallons are missing for the tank to be at maximum capacity again?"""

    # Define the maximum capacity of the tank and the water lost during the first period
    max_capacity = 350000
    lost_first_period = 32000 * 5

    # Calculate the water lost during the second period
    lost_second_period = 10000 * 10

    # Calculate the water added during the third period
    added_third_period = 40000 * 3

    # Calculate the remaining space in the tank after the first two periods
    remaining_space = max_capacity - lost_first_period - lost_second_period

    # Calculate the missing water after the third period
    missing_water = max_capacity - remaining_space - added_third_period

    # Display the result
    result = missing_water
    return result

print(solution())