def solution():
    """Lucius owns a small business and spends $10 every day on ingredients. He then makes a portion of French Fries and a portion of Poutine and sells them to the market, paying ten percent of his weekly income as tax. If the price of French fries is $12 and the price of Poutine is $8, how much does he earn every week after paying the taxes, selling all his products, and buying all the ingredients?"""
    # Define the cost of ingredients per day
    INGREDIENTS_COST_PER_DAY = 10

    # Define the price of French fries and Poutine
    FRIES_PRICE = 12
    POUTINE_PRICE = 8

    # Calculate the total revenue from selling all the products
    fries_revenue = FRIES_PRICE * 7
    poutine_revenue = POUTINE_PRICE * 7
    total_revenue = fries_revenue + poutine_revenue

    # Calculate the total cost of ingredients for the week
    total_ingredients_cost = INGREDIENTS_COST_PER_DAY * 7

    # Calculate the taxable income
    taxable_income = total_revenue - total_ingredients_cost

    # Calculate the tax
    tax = taxable_income * 0.1

    # Calculate the net income
    net_income = total_revenue - total_ingredients_cost - tax

    # Display the net income
    result = net_income
    return result

print(solution())