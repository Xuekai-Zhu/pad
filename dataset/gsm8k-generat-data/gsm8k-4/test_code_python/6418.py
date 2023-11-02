def solution():
    """Macy has a goal of running a total of 24 miles per week. If she runs 3 miles per day, how many miles does Macy have left to run after 6 days so that she could meet her goal?"""
    # Define Macy's weekly goal and her daily distance
    weekly_goal = 24
    daily_distance = 3

    # Calculate the total distance Macy has run after 6 days
    total_distance = daily_distance * 6

    # Calculate the remaining distance Macy needs to run to meet her weekly goal
    remaining_distance = weekly_goal - total_distance

    # return the result
    result = remaining_distance
    return result

print(solution())