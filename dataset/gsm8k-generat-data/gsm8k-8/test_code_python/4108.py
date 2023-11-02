def solution():
    # Calculate the total time Justin has before the movie
    total_time = 3 * 60  # 3 hours in minutes

    # Subtract the time he'll spend at baseball practice and for dinner
    total_time -= 5 * 60  # 5 pm is when he gets home
    total_time -= 45  # 45 minutes for dinner

    # Subtract the time he'll spend on each chore
    total_time -= 30  # Homework
    total_time -= 30  # Cleaning his room
    total_time -= 5  # Taking out the trash
    total_time -= 10  # Emptying the dishwasher

    # Calculate the latest time to begin his chores and homework
    latest_start = 8 * 60 - total_time
    result = latest_start
    return result

print(solution())