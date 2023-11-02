def solution():
    """Alexa has a lemonade stand where she sells lemonade for $2 for one cup. If she spent $20 on ingredients, how many cups of lemonade does she need to sell to make a profit of $80?"""
    price_per_cup = 2
    ingredient_cost = 20
    desired_profit = 80
    cups_needed = (desired_profit + ingredient_cost) / price_per_cup
    result = cups_needed
    return result

print(solution())