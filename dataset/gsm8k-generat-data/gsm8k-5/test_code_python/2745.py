def solution():
    total_doughnuts = 50  # 50 doughnuts were served
    num_staff = 19  # There are 19 staff members
    doughnuts_per_staff = 2  # Each staff member ate 2 doughnuts

    # Calculate the number of doughnuts eaten by the staff
    doughnuts_eaten = num_staff * doughnuts_per_staff

    # Calculate the number of doughnuts left
    doughnuts_left = total_doughnuts - doughnuts_eaten
    result = doughnuts_left
    return result

print(solution())