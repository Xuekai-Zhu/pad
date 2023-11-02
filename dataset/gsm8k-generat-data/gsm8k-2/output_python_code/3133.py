def solution():
    """Toby wants to walk an average of 9,000 steps per day over the next week. On Sunday he walked 9,400 steps. On Monday he walked 9,100 steps. On Tuesday he walked 8,300 steps. On Wednesday he walked 9,200 steps. On Thursday he walked 8,900 steps. How many steps does he need to average on Friday and Saturday to meet his goal?"""
    goal_steps = 9000 * 7
    total_steps = 9400 + 9100 + 8300 + 9200 + 8900
    remaining_steps = goal_steps - total_steps
    remaining_days = 2
    average_needed = remaining_steps / remaining_days
    result = average_needed
    return result

print(solution())