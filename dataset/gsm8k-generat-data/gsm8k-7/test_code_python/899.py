def solution():
    hours_per_day = 8
    hours_per_chair = 5
    num_days = 10

    # Calculate the total number of hours Ben will work in 10 days
    total_hours_worked = hours_per_day * num_days

    # Calculate the maximum number of chairs Ben can build in 10 days given his work hours
    max_num_chairs = total_hours_worked // hours_per_chair

    result = max_num_chairs
    return result

print(solution())