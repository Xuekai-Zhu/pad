def solution():
    """The largest frog can grow to weigh 10 times as much as the smallest frog. The largest frog weighs 120 pounds. How much more does the largest frog weigh than the smallest frog?"""
    # Define the weight of the largest frog
    largest_weight = 120

    # Calculate the weight of the smallest frog
    smallest_weight = largest_weight / 10

    # Calculate the weight difference between the largest and smallest frogs
    weight_difference = largest_weight - smallest_weight

    # Return the result
    result = weight_difference
    return result

print(solution())