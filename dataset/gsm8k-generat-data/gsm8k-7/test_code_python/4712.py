def solution():
    # Distance and speed in miles and hours
    walk_distance = 3
    walk_speed = 3
    run_distance = 10
    run_speed = 5

    # Weight in pounds
    weight = 25

    # Calculate the time it takes to walk 3 miles with a 25-pound backpack
    walk_time = walk_distance / walk_speed

    # Calculate the time it takes to run 10 miles without a backpack
    run_time = run_distance / run_speed

    # Calculate the total time spent exercising each day
    total_time = walk_time + run_time

    # Calculate the total time spent exercising each week
    total_weekly_time = total_time * 7

    result = total_weekly_time
    return result

print(solution())