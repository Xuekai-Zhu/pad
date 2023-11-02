def solution():
    """If a basket is capable of holding 40 fruit altogether, and there are 3 times as many apples as oranges, how many oranges are there?"""
    total_fruits = 40
    apple_ratio = 3
    total_ratio = apple_ratio + 1
    orange_count = total_fruits // total_ratio
    result = orange_count
    return result

print(solution())