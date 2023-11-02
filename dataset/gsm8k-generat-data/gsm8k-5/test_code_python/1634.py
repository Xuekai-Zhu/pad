def solution():
    cost_of_ingredients = 20  # Alexa spent $20 on ingredients
    price_per_cup = 2  # Alexa sells lemonade for $2 per cup
    desired_profit = 80  # Alexa wants to make a profit of $80

    # Calculate the number of cups of lemonade Alexa needs to sell to make a profit of $80
    cups_needed = (desired_profit + cost_of_ingredients) / price_per_cup
    result = cups_needed
    return result

print(solution())