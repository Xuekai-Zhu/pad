def solution():
    time_per_skirt = 2
    time_per_coat = 7
    num_skirts = 6
    num_coats = 4

    # Calculate the total time to sew all skirts
    total_skirt_time = num_skirts * time_per_skirt

    # Calculate the total time to sew all coats
    total_coat_time = num_coats * time_per_coat

    # Calculate the total time to sew all items
    total_time = total_skirt_time + total_coat_time
    result = total_time
    return result

print(solution())