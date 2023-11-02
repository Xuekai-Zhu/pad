def solution():
    """Stella and Twinkle are filling up a truck with a capacity of 6000 stone blocks at the rate of 250 blocks per hour per person. They work for four hours and are then joined by 6 other people who also work at the same rate. How many hours did filling the truck take?"""
    # Define the capacity of the truck and the rate of filling by one person
    truck_capacity = 6000
    filling_rate = 250  # blocks per hour per person

    # Calculate the total number of blocks filled by Stella and Twinkle in 4 hours
    blocks_filled_by_two = 2 * filling_rate * 4

    # Calculate the number of blocks that still need to be filled
    blocks_remaining = truck_capacity - blocks_filled_by_two

    # Calculate the total number of people filling the truck including Stella and Twinkle
    total_people = 8

    # Calculate the time required to fill the remaining blocks with all people working at the same rate
    time_required = blocks_remaining / (total_people * filling_rate)

    # Add the time taken by Stella and Twinkle (4 hours) to get the total time taken
    total_time = time_required + 4

    # return the result
    result = total_time
    return result

print(solution())