def solution():
    num_doughnuts = 50
    num_staff = 19
    num_doughnuts_per_staff = 2

    # Calculate the total number of doughnuts eaten
    total_doughnuts_eaten = num_staff * num_doughnuts_per_staff

    # Calculate the number of doughnuts left
    num_doughnuts_left = num_doughnuts - total_doughnuts_eaten
    result = num_doughnuts_left
    return result

print(solution())