def solution():
    gallon = 4
    dexter_used = 3/8
    jay_used = 5/8
    dexter_liters = gallon * dexter_used
    jay_liters = gallon * jay_used
    total_liters_used = dexter_liters + jay_liters
    liters_left = gallon - total_liters_used
    result = liters_left
    return result

print(solution())