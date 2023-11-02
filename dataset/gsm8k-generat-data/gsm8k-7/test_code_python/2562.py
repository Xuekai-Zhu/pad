def solution():
    num_potatoes = 27
    time_per_three_potatoes = 20/60  # from minutes to hours

    # Calculate how many groups of three potatoes Jason will eat
    num_groups = num_potatoes // 3

    # Calculate the total time it will take Jason to eat all the potatoes
    total_time = num_groups * time_per_three_potatoes

    result = total_time
    return result

print(solution())