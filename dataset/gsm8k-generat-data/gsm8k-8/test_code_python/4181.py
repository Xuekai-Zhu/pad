def solution():
    # Initialize variables
    saved = 4
    total_saved = saved

    # Loop through weeks 2-4 to calculate savings and add to total
    for week in range(2, 5):
        saved *= 2
        total_saved += saved

    # Calculate how much Hannah needs to save in week 5 to reach her goal
    goal = 80
    saved_in_week_5 = goal - total_saved

    result = saved_in_week_5
    return result

print(solution())