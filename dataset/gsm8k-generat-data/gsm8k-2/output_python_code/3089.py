def solution():
    """OpenAI runs a robotics competition that limits the weight of each robot. Each robot can be no more than twice the minimum weight and no less than 5 pounds heavier than the standard robot. The standard robot weighs 100 pounds. What is the maximum weight of a robot in the competition?"""
    standard_weight = 100
    min_weight = standard_weight + 5
    max_weight = 2 * min_weight
    result = max_weight
    return result

print(solution())