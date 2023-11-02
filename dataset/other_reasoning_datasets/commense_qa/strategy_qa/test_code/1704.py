def solution():
    goblin_shark_weight = 460
    bike_weight_capacity = 300
    if goblin_shark_weight <= bike_weight_capacity:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())