def solution():
    time_to_dig_adult_grave = 3  # Dan takes 3 hours to dig an adult grave
    time_to_dig_child_grave = 2  # Dan takes 2 hours to dig a child's grave
    num_adult_graves = 5
    num_child_graves = 1

    # Calculate the total time to dig all the graves
    total_time = (time_to_dig_adult_grave * num_adult_graves) + (time_to_dig_child_grave * num_child_graves)
    result = total_time
    return result

print(solution())