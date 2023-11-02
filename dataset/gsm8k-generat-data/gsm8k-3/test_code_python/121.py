def solution():
    """Stella and Twinkle are filling up a truck with a capacity of 6000 stone blocks at the rate of 250 blocks per hour per person. They work for four hours and are then joined by 6 other people who also work at the same rate. How many hours did filling the truck take?"""
    # Define the capacity of the truck and the rate of filling per person per hour
    TRUCK_CAPACITY = 6000
    FILLING_RATE = 250

    # Define the number of people initially filling the truck and the number of hours they worked
    initial_people = 2
    initial_hours = 4

    # Calculate the total number of blocks filled in the initial period
    initial_blocks_filled = initial_people * FILLING_RATE * initial_hours

    # Calculate the remaining blocks to be filled
    remaining_blocks = TRUCK_CAPACITY - initial_blocks_filled

    # Calculate the number of people working after the initial period
    additional_people = 6

    # Calculate the total number of people working
    total_people = initial_people + additional_people

    # Calculate the total number of hours needed to fill the remaining blocks
    total_hours = remaining_blocks / (total_people * FILLING_RATE)

    # Add the initial hours to the total hours
    total_time = initial_hours + total_hours

    # Display the result
    result = total_time
    return result

print(solution())