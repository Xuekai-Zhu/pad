def solution():
    speed = 6 # miles per hour
    monday_time = 1 # hour
    tuesday_time = 0.5 # hour
    wednesday_time = 1 # hour
    thursday_time = 0.33 # hour
    target_distance = 20 # miles
    remaining_distance = target_distance - (speed * (monday_time + tuesday_time + wednesday_time + thursday_time))

    # Calculate the time needed to run the remaining distance on Friday
    friday_time = remaining_distance / speed * 60 # in minutes
    result = friday_time
    return result

print(solution())