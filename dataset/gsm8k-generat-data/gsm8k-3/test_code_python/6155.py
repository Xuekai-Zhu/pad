def solution():
    """A pickup truck can fill 20 eight gallon water cans (each can filled three quarters of its capacity) in three hours. If each can is filled to full capacity instead, how long, in hours, will it take to fill 25 cans?"""

    # Define the total capacity of each water can
    can_capacity = 8

    # Define the fraction of capacity filled in each can
    fill_fraction = 0.75

    # Define the total number of cans to be filled
    total_cans = 25

    # Find the total amount of water to be filled
    total_water = can_capacity * fill_fraction * total_cans

    # Find the rate of water filling in gallons per hour
    rate = (can_capacity * fill_fraction * 20) / 3

    # Find the time required to fill the total amount of water
    time = total_water / (can_capacity * 1.0)

    # Find the time required to fill 25 cans at full capacity
    time_full = (can_capacity * total_cans) / rate

    # Return the time required to fill 25 cans at full capacity
    result = time_full
    return result

print(solution())