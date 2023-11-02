def solution():
    capacity = 6000  # Capacity of the truck in stone blocks
    rate_per_person = 250  # Rate of filling the truck per person per hour
    initial_time = 4  # Initial time taken by Stella and Twinkle to fill the truck
    initial_people = 2  # Initial number of people filling the truck
    additional_people = 6  # Additional number of people joining later

    # Calculate the initial number of blocks filled by Stella and Twinkle
    initial_blocks_filled = initial_people * rate_per_person * initial_time

    # Calculate the remaining number of blocks needed to fill the truck
    remaining_blocks = capacity - initial_blocks_filled

    # Calculate the total rate of filling the truck per hour after the additional people join
    total_rate = (initial_people + additional_people) * rate_per_person

    # Calculate the time taken to fill the remaining blocks
    remaining_time = remaining_blocks / total_rate

    # Calculate the total time taken to fill the truck
    total_time = initial_time + remaining_time
    result = total_time
    return result

print(solution())