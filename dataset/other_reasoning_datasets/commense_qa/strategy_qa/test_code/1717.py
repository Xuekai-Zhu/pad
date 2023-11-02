def solution():
    distance = 505 # miles
    speed = 105 # MPH
    max_time = distance / speed # hours
    if max_time <= 6:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())