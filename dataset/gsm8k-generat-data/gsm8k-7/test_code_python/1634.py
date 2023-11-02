def solution():
    price_per_cup = 2
    cost_of_ingredients = 20
    desired_profit = 80

    # Calculate the number of cups of lemonade Alexa needs to sell to break even
    cups_to_break_even = cost_of_ingredients / price_per_cup

    # Calculate the total revenue needed to make the desired profit
    total_revenue = cost_of_ingredients + desired_profit

    # Calculate the number of cups of lemonade Alexa needs to sell to make the desired profit
    cups_to_make_profit = total_revenue / price_per_cup
    result = cups_to_make_profit - cups_to_break_even
    return result

print(solution())