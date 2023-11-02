def solution():
    """Rachel weighs 75 pounds, 6 pounds less than Jimmy and 15 pounds more than Adam. What is the average weight of the three people, in pounds?"""
    jimmy_weight = 75 + 6
    adam_weight = 75 - 15
    total_weight = jimmy_weight + adam_weight + 75
    average_weight = total_weight / 3
    result = average_weight
    return result

print(solution())