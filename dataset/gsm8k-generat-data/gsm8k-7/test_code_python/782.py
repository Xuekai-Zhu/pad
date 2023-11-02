def solution():
    fabric_available = 56
    fabric_per_dress = 4
    time_per_dress = 3

    # Calculate the maximum number of dresses that Melissa can make
    num_dresses = fabric_available // fabric_per_dress

    # Calculate the total time needed to make all the dresses
    total_time = num_dresses * time_per_dress
    result = total_time
    return result

print(solution())