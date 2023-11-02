def solution():
    total_fabric = 56
    fabric_per_dress = 4
    time_per_dress = 3

    # Calculate how many dresses can be made with the available fabric
    dresses = total_fabric // fabric_per_dress

    # Calculate the total time needed to make all the dresses
    total_time = dresses * time_per_dress
    result = total_time
    return result

print(solution())