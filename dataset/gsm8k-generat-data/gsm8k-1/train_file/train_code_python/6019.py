def solution():
    """Carrie and her mom go to the mall to buy new clothes for school. Carrie buys 4 shirts, 2 pairs of pants, and 2 jackets. Each shirt costs $8. Each pair of pants costs $18. Each jacket costs $60. If Carrie’s mom pays for half of the total cost of all the clothes, how much does Carrie pay for the clothes?"""
    num_shirts = 4
    num_pants = 2
    num_jackets = 2
    cost_shirts = 8
    cost_pants = 18
    cost_jackets = 60

    total_cost = (num_shirts * cost_shirts) + (num_pants * cost_pants) + (num_jackets * cost_jackets)
    carrie_cost = total_cost / 2

    return carrie_cost

print(solution())