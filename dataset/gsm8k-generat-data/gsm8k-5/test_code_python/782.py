def solution():
    total_fabric = 56  # Melissa has 56 square meters of fabric
    fabric_per_dress = 4  # Each dress takes 4 square meters of fabric
    time_per_dress = 3  # Each dress takes 3 hours to make

    # Calculate the number of dresses Melissa can make
    num_dresses = total_fabric // fabric_per_dress

    # Calculate the total time Melissa needs to make the dresses
    total_time = num_dresses * time_per_dress
    result = total_time
    return result

print(solution())