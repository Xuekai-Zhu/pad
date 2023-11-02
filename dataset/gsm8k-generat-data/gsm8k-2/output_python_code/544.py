def solution():
    """There are 18 green leaves on each of the 3 tea leaf plants. One-third of them turn yellow and fall off on each of the tea leaf plants. How many green leaves are left on the tea leaf plants?"""
    initial_leaves = 18
    fallen_leaves = initial_leaves / 3
    remaining_leaves = initial_leaves - fallen_leaves
    total_remaining_leaves = remaining_leaves * 3
    result = total_remaining_leaves
    return result

print(solution())