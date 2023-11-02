def solution():
    num_lines_to_mow = 40
    time_per_line_mowing = 2 # minutes
    num_rows_to_plant = 8
    num_flowers_per_row = 7
    time_per_flower_planting = 0.5 # minutes

    # Calculate the total time spent mowing
    total_mowing_time = num_lines_to_mow * time_per_line_mowing

    # Calculate the total time spent planting flowers
    total_planting_time = num_rows_to_plant * num_flowers_per_row * time_per_flower_planting

    # Calculate the total time spent gardening
    total_time = total_mowing_time + total_planting_time
    result = total_time
    return result

print(solution())