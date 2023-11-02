def solution():
    """The largest frog can grow to weigh 10 times as much as the smallest frog. The largest frog weighs 120 pounds. How much more does the largest frog weigh than the smallest frog?"""
    largest_wt = 120
    smallest_wt = largest_wt / 10
    difference = largest_wt - smallest_wt
    result = difference
    return result

print(solution())