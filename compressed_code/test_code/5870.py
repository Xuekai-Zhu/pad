def solution():
    
    tuesday = 25
    monday = tuesday * 0.8
    wednesday = monday + 2
    thursday = 10
    friday = 10
    weekend = 5 * 2
    total_cars = tuesday + monday + wednesday + thursday + friday + weekend
    result = total_cars
    return result

print(solution())