def solution():
    """Paulo wants to get a burger meal that costs $6. Aside from that, he also wants to get a soda which costs 1/3 as much as the burger meal. While on the counter, Jeremy asked Paulo to get him 2 of each item Paulo is going to get. How much will they be charged for their orders combined?"""
    burger_cost = 6
    soda_cost = burger_cost / 3
    paulo_order = (burger_cost + soda_cost) * 2
    jeremy_order = paulo_order
    total_cost = paulo_order + jeremy_order
    result = total_cost
    return result

print(solution())