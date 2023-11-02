def solution():
    """Kaiden is collecting cans of soup for the local soup kitchen. He collects 158 cans during his first week and 259 during the second week. If his goal is to collect 500 cans how many more cans of soup does he need to collect?"""
    # Define the number of cans collected in the first and second weeks
    cans_week1 = 158
    cans_week2 = 259

    # Define the total goal number of cans
    total_goal_cans = 500

    # Calculate the total number of cans collected
    total_cans_collected = cans_week1 + cans_week2

    # Calculate the number of additional cans needed to reach the goal
    cans_needed = total_goal_cans - total_cans_collected

    # Return the result
    result = cans_needed
    return result

print(solution())