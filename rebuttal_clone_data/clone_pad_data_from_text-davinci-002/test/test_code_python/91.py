def solution():
    
    miles_to_destination = 55
    miles_back = 65
    minutes_per_mile = 2
    minutes_at_destination = 120
    total_minutes = minutes_per_mile * (miles_to_destination + miles_back) + minutes_at_destination
    hours = total_minutes / 60
    result = hours
    return result

print(solution())