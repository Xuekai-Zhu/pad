def solution():
    cans_first_week = 158
    cans_second_week = 259
    goal = 500

    # Calculate the total number of cans collected so far
    total_cans_collected = cans_first_week + cans_second_week

    # Calculate the number of cans still needed to reach the goal
    cans_needed = goal - total_cans_collected
    result = cans_needed
    return result

print(solution())