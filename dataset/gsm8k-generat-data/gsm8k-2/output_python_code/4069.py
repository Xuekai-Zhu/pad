def solution():
    """Lucius owns a small business and spends $10 every day on ingredients. He then makes a portion of French Fries and a portion of Poutine and sells them to the market, paying ten percent of his weekly income as tax. If the price of French fries is $12 and the price of Poutine is $8, how much does he earn every week after paying the taxes, selling all his products, and buying all the ingredients?"""
    ingredient_cost_per_day = 10
    french_fries_price = 12
    poutine_price = 8
    french_fries_profit = french_fries_price - ingredient_cost_per_day
    poutine_profit = poutine_price - ingredient_cost_per_day
    total_profit_per_day = french_fries_profit + poutine_profit
    total_profit_per_week = 7 * total_profit_per_day
    tax = 0.1 * total_profit_per_week
    final_profit = total_profit_per_week - tax
    result = final_profit
    return result

print(solution())