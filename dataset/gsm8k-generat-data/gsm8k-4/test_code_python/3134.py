def solution():
    """Toby wants to walk an average of 9,000 steps per day over the next week. On Sunday he walked 9,400 steps. On Monday he walked 9,100 steps. On Tuesday he walked 8,300 steps. On Wednesday he walked 9,200 steps. On Thursday he walked 8,900 steps. How many steps does he need to average on Friday and Saturday to meet his goal?"""
    # Define the total number of steps Toby wants to walk in a week
    GOAL_STEPS = 9000 * 7

    # Calculate the number of steps Toby has walked so far
    steps_so_far = 9400 + 9100 + 8300 + 9200 + 8900

    # Calculate the number of steps Toby needs to walk on Friday and Saturday
    remaining_steps = GOAL_STEPS - steps_so_far
    remaining_days = 7 - 5
    avg_steps = remaining_steps / remaining_days

    # Round the result to the nearest whole number
    result = round(avg_steps)
    return result

print(solution())