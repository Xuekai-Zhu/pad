def solution():
    """There are three times as many hogs as cats in King Henry's kingdom. If there are 75 hogs, what's 5 less than 60% of the number of cats in King Henry's kingdom?"""
    num_hogs = 75
    num_cats = num_hogs / 3
    cat_percent = 60
    cat_percent_less = cat_percent - 5
    cat_percent_decimal = cat_percent_less / 100
    cat_amount = cat_percent_decimal * num_cats
    result = cat_amount - 5
    return result

print(solution())