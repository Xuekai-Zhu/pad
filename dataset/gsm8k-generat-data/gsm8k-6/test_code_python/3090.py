def solution():
    # Calculate the minimum weight of a robot
    min_weight = 100 + 5  # standard robot weighs 100 pounds and is at least 5 pounds heavier
    # Calculate the maximum weight of a robot
    max_weight = 2 * min_weight  # each robot can be no more than twice the minimum weight
    result = max_weight
    return result

print(solution())