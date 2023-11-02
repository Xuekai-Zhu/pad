def solution():
    
    richard_time = 22
    cory_time = richard_time + 3
    blake_time = cory_time - 4
    rooms_cleaned = 2
    total_time = (richard_time + cory_time + blake_time) * rooms_cleaned
    result = total_time
    return result

print(solution())