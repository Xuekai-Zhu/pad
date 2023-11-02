def solution():
    """Tony exercises every morning by walking 3 miles carrying a 25-pound backpack, then he runs another 10 miles without the backpack. If he walks at a speed of 3 miles per hour and runs at a speed of 5 miles per hour, how many hours each week does he spend exercising?"""
    # Define the distance, speed, and time for walking
    walk_distance = 3
    walk_speed = 3
    walk_time = walk_distance / walk_speed

    # Define the distance, speed, and time for running
    run_distance = 10
    run_speed = 5
    run_time = run_distance / run_speed

    # Define the total time spent exercising each day
    total_time = walk_time + run_time

    # Define the number of days in a week and calculate the total time spent exercising each week
    days_per_week = 7
    total_time_weekly = total_time * days_per_week

    result = total_time_weekly
    return result

print(solution())