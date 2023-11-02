def solution():
    """Kiaan is doing home delivery of newspapers in his neighborhood of 200 homes. After an hour of work, he has distributed newspapers to 2/5 of the homes. After another 2 hours of working, he realizes he has distributed newspapers to 60 percent of the remaining homes. How many homes does he still need to distribute the newspapers to?"""
    total_homes = 200
    homes_delivered_first_hour = total_homes * (2/5)
    homes_remaining_after_first_hour = total_homes - homes_delivered_first_hour
    homes_delivered_second_hour = homes_remaining_after_first_hour * 0.6
    homes_remaining = total_homes - homes_delivered_first_hour - homes_delivered_second_hour
    result = homes_remaining
    return result

print(solution())