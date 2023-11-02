def solution():
    distance_one_way = 0.5
    num_days_per_week = 5
    num_weeks = 4

    # Calculate the total distance Wanda walks one way per day
    total_distance_one_way = distance_one_way * 2

    # Calculate the total distance Wanda walks to and from school per day
    total_distance_per_day = total_distance_one_way * num_days_per_week

    # Calculate the total distance Wanda walks in 4 weeks
    total_distance = total_distance_per_day * num_weeks
    result = total_distance
    return result

print(solution())