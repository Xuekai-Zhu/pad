def solution():
    """Tracy, John and Jake found their combined weight to be 158 kilograms. If Tracy weighs 52 kg and Jake weighs 8kg more than Tracy, what is the range of their weights?"""
    # Define Tracy's weight
    tracy_weight = 52

    # Calculate Jake's weight, which is 8kg more than Tracy's weight
    jake_weight = tracy_weight + 8

    # Calculate John's weight
    john_weight = 158 - tracy_weight - jake_weight

    # Find the minimum and maximum weight among the three
    min_weight = min(tracy_weight, john_weight, jake_weight)
    max_weight = max(tracy_weight, john_weight, jake_weight)

    # Return the weight range
    result = (min_weight, max_weight)
    return result

print(solution())