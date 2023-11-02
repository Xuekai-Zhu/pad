def solution():
    # Calculate the weight of Jake
    jake_weight = 52 + 8

    # Calculate the weight of John
    john_weight = 158 - jake_weight - 52

    # Find the minimum and maximum weight of the three people
    minimum_weight = min(tracy_weight, john_weight, jake_weight)
    maximum_weight = max(tracy_weight, john_weight, jake_weight)

    result = f"The range of weights is {minimum_weight} kg to {maximum_weight} kg"
    return result

print(solution())