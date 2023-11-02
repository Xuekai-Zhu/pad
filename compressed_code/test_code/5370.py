def solution():
    
    hours_per_day = 6
    days = 5
    total_hours = hours_per_day * days
    total_kilowatts = (total_hours / 8) * 7.2
    result = total_kilowatts
    return result

print(solution())