def solution():
    """48 children are trying to share a pack of sweets. After taking 4 sweets each, there is still a third of the original amount left. What is the original number of sweets in the pack?"""
    children = 48
    sweets_per_child = 4
    remaining_sweets = (1/3) * (children * sweets_per_child)
    original_sweets = remaining_sweets * 3
    result = original_sweets
    return result

print(solution())