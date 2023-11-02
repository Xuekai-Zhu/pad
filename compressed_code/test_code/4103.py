def solution():
    
    num_children = 3
    num_hours = 4
    num_houses_per_hour = 5
    num_treats_per_house = 3
    num_treats_per_child = num_houses_per_hour * num_treats_per_house
    total_treats = num_treats_per_child * num_children * num_hours
    result = total_treats
    return result

print(solution())