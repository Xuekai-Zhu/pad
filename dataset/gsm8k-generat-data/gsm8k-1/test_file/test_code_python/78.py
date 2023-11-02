def solution():
    """Grace weighs 125 pounds. Alex weighs 2 pounds less than 4 times what Grace weighs. What are their combined weights in pounds?"""
    grace_weight = 125
    alex_weight = (4 * grace_weight) - 2
    total_weight = grace_weight + alex_weight
    result = total_weight
    return result

print(solution())