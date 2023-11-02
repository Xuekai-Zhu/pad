def solution():
    """If Billy and Jenny each order a $20 steak along with a $5 drink, how much will Billy have to pay in tips if he wants to cover 80% of a 20% tip for the two of them?"""
    meal_cost = 40 + 10  # 20 for each steak and 5 for each drink
    tip_percentage = 20
    tip_coverage = 0.8
    tip_amount = meal_cost * (tip_percentage / 100) * (1 / 2) * tip_coverage
    billy_tip = tip_amount
    return billy_tip

print(solution())