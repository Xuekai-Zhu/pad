def solution():
    """If Billy and Jenny each order a $20 steak along with a $5 drink, how much will Billy have to pay in tips if he wants to cover 80% of a 20% tip for the two of them?"""
    steak_cost = 20
    drink_cost = 5
    total_cost = (steak_cost * 2) + (drink_cost * 2)
    tip_percent = 20
    tip_amount = total_cost * (tip_percent / 100)
    billy_tip_amount = tip_amount * 0.8
    result = billy_tip_amount
    return result

print(solution())