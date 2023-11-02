def solution():
    # Define the weights of Tracy and Jake
    tracy_weight = 52
    jake_weight = tracy_weight + 8

    # Calculate the weight of John
    john_weight = 158 - tracy_weight - jake_weight

    # Find the minimum and maximum weight in the group
    minimum_weight = min(tracy_weight, jake_weight, john_weight)
    maximum_weight = max(tracy_weight, jake_weight, john_weight)

    # Calculate the range of their weights
    weight_range = maximum_weight - minimum_weight
    result = weight_range
    return result

print(solution())