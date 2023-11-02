def solution():
    """During a staff meeting, 50 doughnuts were served. If each of the 19 staff ate 2 doughnuts, how many doughnuts are left?"""
    num_staff = 19
    num_doughnuts_per_staff = 2
    total_doughnuts_served = 50
    num_doughnuts_eaten = num_staff * num_doughnuts_per_staff
    num_doughnuts_left = total_doughnuts_served - num_doughnuts_eaten
    result = num_doughnuts_left
    return result

print(solution())