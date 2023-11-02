def solution():
    car_cost = 2100
    sister_use_percentage = 4/7
    sue_use_percentage = 1 - sister_use_percentage
    sue_cost = car_cost * sue_use_percentage
    result = sue_cost
    return result

print(solution())