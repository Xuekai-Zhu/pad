def solution():
    """Alexa has a lemonade stand where she sells lemonade for $2 for one cup. If she spent $20 on ingredients, how many cups of lemonade does she need to sell to make a profit of $80?"""
    lemonade_cost = 20
    profit_goal = 80
    cup_price = 2
    cups_needed = (lemonade_cost + profit_goal) / cup_price
    result = cups_needed
    return result

print(solution())