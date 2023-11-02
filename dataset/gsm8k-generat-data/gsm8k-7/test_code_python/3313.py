def solution():
    tea_per_day = 0.2
    box_size = 28

    # Calculate the total amount of tea needed for one week
    total_tea_per_week = tea_per_day * 7

    # Calculate the number of weeks of tea that Marco can get from one box
    num_weeks_per_box = box_size / total_tea_per_week
    result = num_weeks_per_box
    return result

print(solution())