def solution():
    adult_grave_time = 3
    child_grave_time = 2

    num_adult_graves = 5
    num_child_graves = 1

    # Calculate the total time it takes to dig all adult graves
    total_adult_time = adult_grave_time * num_adult_graves

    # Calculate the total time it takes to dig the child's grave
    total_child_time = child_grave_time * num_child_graves

    # Calculate the total time it takes to dig all graves
    total_time = total_adult_time + total_child_time
    result = total_time
    return result

print(solution())