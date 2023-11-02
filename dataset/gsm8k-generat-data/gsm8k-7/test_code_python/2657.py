def solution():
    num_doughnuts_per_dozen = 12
    num_dozen_per_box = 2
    num_doughnuts_per_box = num_doughnuts_per_dozen * num_dozen_per_box

    num_doughnuts_eaten = 8

    # Calculate the number of doughnuts left
    num_doughnuts_left = num_doughnuts_per_box - num_doughnuts_eaten
    result = num_doughnuts_left
    return result

print(solution())