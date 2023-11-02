def solution():
    """OpenAI runs a robotics competition that limits the weight of each robot. Each robot can be no more than twice the minimum weight and no less than 5 pounds heavier than the standard robot. The standard robot weighs 100 pounds. What is the maximum weight of a robot in the competition?"""
    # Define the minimum weight of a robot
    minimum_weight = 100 + 5

    # Calculate the maximum weight of a robot
    maximum_weight = minimum_weight * 2

    # Return the result
    result = maximum_weight
    return result

print(solution())