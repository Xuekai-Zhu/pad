def solution():
    """Jonathan enjoys walking and running for exercise, and he has three different exercise routines. On Mondays, he walks at 2 miles per hour. On Wednesdays, he walks at 3 miles per hour. And on Fridays, he runs at 6 miles per hour. On each exercise day, he travels 6 miles. What is the combined total time, in hours, he spends exercising in a week?"""
    monday_speed = 2
    wednesday_speed = 3
    friday_speed = 6
    distance = 6
    monday_time = distance / monday_speed
    wednesday_time = distance / wednesday_speed
    friday_time = distance / friday_speed
    total_time = monday_time + wednesday_time + friday_time
    result = total_time
    return result

print(solution())