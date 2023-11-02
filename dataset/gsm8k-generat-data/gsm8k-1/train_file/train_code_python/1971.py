def solution():
    """The largest frog can grow to weigh 10 times as much as the smallest frog. The largest frog weighs 120 pounds. How much more does the largest frog weigh than the smallest frog?"""
    largest_weight = 120
    weight_ratio = 10
    smallest_weight = largest_weight / weight_ratio
    weight_difference = largest_weight - smallest_weight
    result = weight_difference
    return result

print(solution())