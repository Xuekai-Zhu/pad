def solution():
    """Lucius owns a small business and spends $10 every day on ingredients. He then makes a portion of French Fries and a portion of Poutine and sells them to the market, paying ten percent of his weekly income as tax. If the price of French fries is $12 and the price of Poutine is $8, how much does he earn every week after paying the taxes, selling all his products, and buying all the ingredients?"""
    # Define the price of French Fries and Poutine
    french_fries_price = 12
    poutine_price = 8

    # Define the daily cost of ingredients
    daily_ingredients_cost = 10

    # Calculate the weekly income from selling French Fries and Poutine
    weekly_income = (french_fries_price + poutine_price) * 7

    # Calculate the weekly cost of ingredients
    weekly_ingredients_cost = daily_ingredients_cost * 7

    # Calculate the weekly profit before taxes
    weekly_profit = weekly_income - weekly_ingredients_cost

    # Calculate the amount of tax to be paid
    tax = weekly_profit * 0.1

    # Calculate the weekly profit after taxes
    weekly_profit_after_tax = weekly_profit - tax

    # return the result
    result = weekly_profit_after_tax
    return result

print(solution())