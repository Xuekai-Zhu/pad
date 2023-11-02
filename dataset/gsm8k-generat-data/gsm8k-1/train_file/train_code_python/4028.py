def solution():
    """To raise money, a school is selling ice-pops for $1.50. It costs 90 cents to make each pop, 
    and the money from the pops will be used to buy pencils, which cost $1.80 each. 
    How many pops must be sold to buy 100 pencils?"""
    pops_price = 1.5
    pops_cost = 0.9
    pencils_price = 1.8
    pens_needed = 100
    money_needed = pens_needed * pencils_price
    pops_needed = money_needed / (pops_price - pops_cost)
    result = pops_needed
    return result

print(solution())