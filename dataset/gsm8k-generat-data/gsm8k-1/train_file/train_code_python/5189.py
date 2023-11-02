def solution():
    """Kiaan is doing home delivery of newspapers in his neighbourhood of 200 homes. After an hour of work, he has distributed newspapers to 2/5 of the homes. After another 2 hours of working, he realizes he has distributed newspapers to 60 percent of the remaining homes. How many homes does he still need to distribute the newspapers to?"""
    total_homes = 200
    homes_distributed_first_hour = 2/5 * total_homes
    homes_remaining = total_homes - homes_distributed_first_hour
    homes_distributed_second_hour = 0.6 * homes_remaining
    homes_left = homes_remaining - homes_distributed_second_hour
    result = homes_left
    return result

print(solution())