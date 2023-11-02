def solution():
    # Convert the dimensions of the land from feet to yards
    length = 200/3
    width = 900/3
    total_area = length * width  # Total area of land in square yards
    area_cleared_per_day = 10*9  # Ten square yards of lawn area cleared per day by one rabbit
    total_area_cleared_per_day = area_cleared_per_day * 100  # Total area cleared per day by 100 rabbits
    days_to_clear_all_grass = total_area / total_area_cleared_per_day

    result = days_to_clear_all_grass
    return result

print(solution())