def solution():
    """Violet has 3 more than twice as many nails as Tickletoe. If Violet has 27 nails, how many nails do they have together?"""
    violet_nails = 27
    t_nails = (violet_nails - 3) / 2
    total_nails = violet_nails + t_nails
    result = total_nails
    return result

print(solution())