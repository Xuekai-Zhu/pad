def solution():
    """Tony exercises every morning by walking 3 miles carrying a 25-pound backpack, then he runs another 10 miles without the backpack. If he walks at a speed of 3 miles per hour and runs at a speed of 5 miles per hour, how many hours each week does he spend exercising?"""
    # Calculate walking time
    walking_distance = 3
    walking_speed = 3
    walking_time = walking_distance / walking_speed

    # Calculate running time
    running_distance = 10
    running_speed = 5
    running_time = running_distance / running_speed

    # Calculate total exercise time per day
    total_time = walking_time + running_time

    # Calculate total exercise time per week
    days_per_week = 7
    total_weekly_time = total_time * days_per_week

    result = total_weekly_time
    return result

print(solution())