def solution():
    capacity = 6000
    rate_per_person = 250
    num_people_initial = 2
    num_people_added = 6
    hours_initial = 4

    # Calculate the total number of blocks filled by Stella and Twinkle in the first 4 hours
    num_blocks_initial = num_people_initial * rate_per_person * hours_initial

    # Calculate the total number of blocks filled by the entire team after the first 4 hours
    num_blocks_remaining = capacity - num_blocks_initial
    rate_total = (num_people_initial + num_people_added) * rate_per_person
    hours_remaining = num_blocks_remaining / rate_total

    # Calculate the total time taken to fill the truck
    total_hours = hours_initial + hours_remaining
    result = total_hours
    return result

print(solution())