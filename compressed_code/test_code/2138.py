def solution():
    
    num_staff = 19
    num_doughnuts_per_staff = 2
    total_doughnuts_served = 50
    num_doughnuts_eaten = num_staff * num_doughnuts_per_staff
    num_doughnuts_left = total_doughnuts_served - num_doughnuts_eaten
    result = num_doughnuts_left
    return result

print(solution())