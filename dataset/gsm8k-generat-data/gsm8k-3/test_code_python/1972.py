def solution():
    """The largest frog can grow to weigh 10 times as much as the smallest frog. The largest frog weighs 120 pounds. How much more does the largest frog weigh than the smallest frog?"""
    # Define the weight of the largest frog
    largest_frog_weight = 120

    # Calculate the weight of the smallest frog
    smallest_frog_weight = largest_frog_weight / 10

    # Calculate the difference between the two weights
    weight_difference = largest_frog_weight - smallest_frog_weight

    # Display the weight difference
    result = weight_difference
    return result

print(solution())