def solution():
    
    time_per_house = 20  
    hours_available = 3
    houses_painted = (hours_available * 60) // time_per_house
    result = houses_painted
    return result

print(solution())