def solution():
    """48 children are trying to share a pack of sweets. After taking 4 sweets each, there is still a third of the original amount left. What is the original number of sweets in the pack?"""
    children = 48
    sweets_per_child = 4
    remaining_sweets_percent = 1/3
    total_sweets = children * sweets_per_child + (children * sweets_per_child / (1 - remaining_sweets_percent))
    result = total_sweets
    return result

print(solution())