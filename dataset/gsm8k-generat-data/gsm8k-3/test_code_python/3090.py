def solution():
    """OpenAI runs a robotics competition that limits the weight of each robot. Each robot can be no more than twice the minimum weight and no less than 5 pounds heavier than the standard robot. The standard robot weighs 100 pounds. What is the maximum weight of a robot in the competition?"""
    # Define the weight of the standard robot and the weight limit
    standard_weight = 100
    weight_limit = 2 * (standard_weight + 5)

    # Calculate the maximum weight of a robot
    max_weight = min(weight_limit, 2 * standard_weight)

    # Display the maximum weight
    result = max_weight
    return result

print(solution())