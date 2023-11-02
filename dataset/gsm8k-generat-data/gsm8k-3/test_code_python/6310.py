def solution():
    """Tracy, John and Jake found their combined weight to be 158 kilograms. If Tracy weighs 52 kg and Jake weighs 8kg more than Tracy, what is the range of their weights?"""
    # Tracy's weight
    tracy_weight = 52

    # Jake's weight
    jake_weight = tracy_weight + 8

    # John's weight
    john_weight = 158 - tracy_weight - jake_weight

    # Determine the range of their weights
    minimum_weight = min(tracy_weight, jake_weight, john_weight)
    maximum_weight = max(tracy_weight, jake_weight, john_weight)

    # Display the range of their weights
    result = (minimum_weight, maximum_weight)
    return result

print(solution())