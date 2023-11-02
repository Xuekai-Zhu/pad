def solution():
    """The ratio of boys to girls in a family is 5:7. The total number of children in the family is 180. If the boys are given $3900 to share, how much money does each boy receive?"""
    total_ratio = 5 + 7
    boys_ratio = 5 / total_ratio
    boys_count = boys_ratio * 180
    amount_per_boy = 3900 / boys_count
    result = amount_per_boy
    return result

print(solution())