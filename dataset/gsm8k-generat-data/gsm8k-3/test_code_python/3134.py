def solution():
    """Toby wants to walk an average of 9,000 steps per day over the next week. On Sunday he walked 9,400 steps. On Monday he walked 9,100 steps. On Tuesday he walked 8,300 steps. On Wednesday he walked 9,200 steps. On Thursday he walked 8,900 steps. How many steps does he need to average on Friday and Saturday to meet his goal?"""
    # Define the total number of steps Toby wants to walk over the week
    TOTAL_GOAL = 9000 * 7

    # Define the number of steps Toby has already walked
    steps_walked = 9400 + 9100 + 8300 + 9200 + 8900

    # Calculate the number of steps Toby needs to walk on Friday and Saturday to reach his goal
    steps_remaining = TOTAL_GOAL - steps_walked
    days_remaining = 7 - 5 # Toby has already walked for 5 days
    steps_per_day_remaining = steps_remaining / days_remaining

    # Display the number of steps Toby needs to walk on Friday and Saturday
    result = steps_per_day_remaining
    return result

print(solution())