def solution():
    """Mrs. Jameson's bamboo in the backyard grows up to 30 inches a day. Today, its height is 20 feet. In how many days will its height be 600 inches?"""
    current_height = 20 * 12
    target_height = 600
    growth_per_day = 30
    days_to_reach_target = (target_height - current_height) / growth_per_day
    result = days_to_reach_target
    return result

print(solution())