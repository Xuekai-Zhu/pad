def solution():
    """The ratio of boys to girls in a family is 5:7. The total number of children in the family is 180. If the boys are given $3900 to share, how much money does each boy receive?"""
    total_children = 180
    boys_ratio = 5
    girls_ratio = 7
    total_ratio = boys_ratio + girls_ratio
    boys_count = total_children * (boys_ratio / total_ratio)
    boys_share = 3900 / boys_count
    result = boys_share
    return result

print(solution())