def solution():
    """One hundred chips were divided by Ian and Lyle in the ratio 4:6. What percentage of the chips did Lyle have?"""
    total_chips = 100
    lyle_ratio = 6
    total_ratio = 4 + 6
    lyle_fraction = lyle_ratio / total_ratio
    lyle_percentage = lyle_fraction * 100
    result = lyle_percentage
    return result

print(solution())