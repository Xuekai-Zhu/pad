def solution():
    max_dogs = 3
    short_walk_time = 30 # in minutes
    short_walk_pay = 15
    long_walk_time = 60 # in minutes
    long_walk_pay = 20
    work_hours_per_day = 4
    num_long_walks_per_day = 6
    num_days_worked = 5

    # Calculate the total number of walks Johnny can do per day
    total_walks_per_day = work_hours_per_day * 60 / short_walk_time
    # Calculate the total number of long walks Johnny will do per day
    total_long_walks_per_day = min(num_long_walks_per_day, total_walks_per_day // max_dogs)
    # Calculate the total number of short walks Johnny will do per day
    total_short_walks_per_day = total_walks_per_day - total_long_walks_per_day * max_dogs
    # Calculate the total pay Johnny will receive per day
    total_pay_per_day = total_long_walks_per_day * long_walk_pay + total_short_walks_per_day * short_walk_pay
    # Calculate the total pay Johnny will receive for the week
    total_pay_for_week = total_pay_per_day * num_days_worked

    result = total_pay_for_week
    return result

print(solution())