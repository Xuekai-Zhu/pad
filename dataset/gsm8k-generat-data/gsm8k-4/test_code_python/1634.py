def solution():
    """Alexa has a lemonade stand where she sells lemonade for $2 for one cup. If she spent $20 on ingredients, how many cups of lemonade does she need to sell to make a profit of $80?"""
    # Define the lemonade price and the cost of ingredients
    lemonade_price = 2
    ingredients_cost = 20

    # Calculate the profit per cup of lemonade
    profit_per_cup = lemonade_price - (ingredients_cost / 100)

    # Calculate the number of cups of lemonade needed to make a profit of $80
    cups_needed = 80 / profit_per_cup

    # Round up to the nearest integer
    cups_needed = int(cups_needed) + 1

    result = cups_needed
    return result

print(solution())