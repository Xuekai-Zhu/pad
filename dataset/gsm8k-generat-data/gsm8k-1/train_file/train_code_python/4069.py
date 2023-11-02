def solution():
    """Lucius owns a small business and spends $10 every day on ingredients. He then makes a portion of French Fries and a portion of Poutine and sells them to the market, paying ten percent of his weekly income as tax. If the price of French fries is $12 and the price of Poutine is $8, how much does he earn every week after paying the taxes, selling all his products, and buying all the ingredients?"""
    ingredients_cost = 10 * 7
    french_fries_price = 12
    poutine_price = 8
    
    french_fries_sold = 50
    poutine_sold = 30
    
    total_income = (french_fries_price * french_fries_sold) + (poutine_price * poutine_sold)
    tax = total_income * 0.1
    income_after_tax = total_income - tax
    
    profit = income_after_tax - ingredients_cost
    
    result = profit
    return result

print(solution())