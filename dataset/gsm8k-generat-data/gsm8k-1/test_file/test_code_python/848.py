def solution():
    """A basket of green food costs $25 and a basket of red food costs $18. If you buy 3 baskets of green food and red food, how much will you have to pay in total if you get $2 off for each basket of red food?"""
    green_food_cost = 25
    red_food_cost = 18
    green_baskets = 3
    red_baskets = 3
    total_cost = (green_food_cost * green_baskets) + \
                 ((red_food_cost - 2) * red_baskets)
    result = total_cost
    return result

print(solution())