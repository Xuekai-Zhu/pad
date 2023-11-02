def solution():
    """Harris feeds his dog 1 large organic carrot over the course of 1 day. There are 5 carrots in a 1 pound bag and each bag costs $2.00. In one year, how much will Harris spend on carrots?"""
    carrots_per_day = 1
    pounds_per_carrot = 1/5
    bags_per_year = 365/pounds_per_carrot/5
    cost_per_bag = 2
    total_cost = bags_per_year * cost_per_bag
    result = total_cost
    return result

print(solution())