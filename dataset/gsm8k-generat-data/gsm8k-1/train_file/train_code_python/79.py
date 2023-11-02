def solution():
    """Jennifer purchased 40 cans of milk at the store before meeting her classmate Mark, who was also buying milk. Jennifer bought 6 additional cans for every 5 cans Mark bought. If Mark purchased 50 cans, how many cans of milk did Jennifer bring home from the store?"""
    jennifer_base_cans = 40
    mark_cans = 50
    extra_cans = (mark_cans // 5) * 6
    total_cans = jennifer_base_cans + extra_cans
    result = total_cans
    return result

print(solution())