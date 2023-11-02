def solution():
    
    boys = 40
    girls = boys / 4
    boy_cost = 50
    girl_cost = boy_cost / 2
    total_cost = (boys * boy_cost) + (girls * girl_cost)
    result = total_cost
    return result

print(solution())