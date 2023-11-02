def solution():
    """On an American flag, the first stripe is red and half of the remaining stripes are also red. Each flag has 13 stripes. John buys 10 flags. How many red stripes are there?"""
    total_flags = 10
    total_stripes = total_flags * 13
    red_stripes = 1
    for i in range(1, 13):
        red_stripes += (total_stripes - i) % 2
    result = red_stripes * total_flags
    return result

print(solution())