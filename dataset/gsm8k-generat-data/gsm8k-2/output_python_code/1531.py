def solution():
    """A fixer uses 30% of the nails in a container to repair the kitchen. He also used 70% of the remaining nails in the container to repair the fence.
    If there were 400 nails in the container, how many nails are remaining?"""
    total_nails = 400
    kitchen_nails = total_nails * 0.3
    remaining_nails = total_nails - kitchen_nails
    fence_nails = remaining_nails * 0.7
    remaining_nails = remaining_nails - fence_nails
    result = remaining_nails
    return result

print(solution())