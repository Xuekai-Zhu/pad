def solution():
    """Paulo wants to get a burger meal that costs $6. Aside from that, he also wants to get a soda which costs 1/3 as much as the burger meal. While on the counter, Jeremy asked Paulo to get him 2 of each item Paulo is going to get. How much will they be charged for their orders combined?"""
    burger_price = 6
    soda_price = burger_price / 3
    paulo_total = (burger_price + soda_price) * 2
    jeremy_total = paulo_total
    combined_total = paulo_total + jeremy_total
    result = combined_total
    return result

print(solution())