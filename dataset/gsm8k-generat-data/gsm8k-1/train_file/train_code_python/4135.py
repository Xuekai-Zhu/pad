def solution():
    """Mary uses plastic grocery bags that can hold a maximum of twenty pounds. She buys 4 pounds of green beans, 6 pounds milk, and twice the amount of carrots as green beans. How many more pounds of groceries can Mary fit in that bag?"""
    max_weight = 20
    current_weight = 4 + 6 + (2 * 4)
    remaining_weight = max_weight - current_weight
    result = remaining_weight
    return result

print(solution())