def solution():
    """On an American flag, the first stripe is red and half of the remaining stripes are also red. Each flag has 13 stripes. John buys 10 flags. How many red stripes are there?"""
    total_stripes = 13
    red_stripes = (total_stripes - 1) / 2 + 1
    num_flags = 10
    total_red_stripes = red_stripes * num_flags
    result = total_red_stripes
    return result

print(solution())