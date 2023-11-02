def solution():
    """Carrie and her mom go to the mall to buy new clothes for school. Carrie buys 4 shirts, 2 pairs of pants, and 2 jackets. Each shirt costs $8. Each pair of pants costs $18. Each jacket costs $60. If Carrie’s mom pays for half of the total cost of all the clothes, how much does Carrie pay for the clothes?"""
    num_shirts = 4
    num_pants = 2
    num_jackets = 2
    shirt_cost = 8
    pant_cost = 18
    jacket_cost = 60
    total_cost = (num_shirts * shirt_cost) + (num_pants * pant_cost) + (num_jackets * jacket_cost)
    carrie_share = total_cost / 2
    result = carrie_share
    return result

print(solution())