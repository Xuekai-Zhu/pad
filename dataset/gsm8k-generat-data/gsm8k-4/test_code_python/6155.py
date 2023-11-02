def solution():
    """A pickup truck can fill 20 eight gallon water cans (each can filled three quarters of its capacity) in three hours. If each can is filled to full capacity instead, how long, in hours, will it take to fill 25 cans?"""
    # Define the capacity of each can and the number of cans that can be filled in 3 hours
    can_capacity = 8 * 0.75  # 6 gallons
    cans_filled = 20

    # Calculate the total amount of water filled in 3 hours
    water_filled = can_capacity * cans_filled

    # Calculate the amount of water needed to fill 25 cans to full capacity
    water_needed = 25 * 8

    # Calculate the time needed to fill 25 cans to full capacity
    time_needed = (water_needed / water_filled) * 3

    # Return the result
    result = time_needed
    return result

print(solution())