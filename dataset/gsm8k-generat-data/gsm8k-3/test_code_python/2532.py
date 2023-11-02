def solution():
    """Kaiden is collecting cans of soup for the local soup kitchen. He collects 158 cans during his first week and 259 during the second week. If his goal is to collect 500 cans how many more cans of soup does he need to collect?"""
    # Define the number of cans collected during the first and second week
    cans_first_week = 158
    cans_second_week = 259

    # Define the goal number of cans
    goal_cans = 500

    # Calculate the total number of cans collected
    total_cans = cans_first_week + cans_second_week

    # Calculate the number of additional cans needed to reach the goal
    additional_cans_needed = goal_cans - total_cans

    # Display the number of additional cans needed
    result = additional_cans_needed
    return result

print(solution())