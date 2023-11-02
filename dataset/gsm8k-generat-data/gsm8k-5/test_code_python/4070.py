def solution():
    daily_ingredient_cost = 10  # Lucius spends $10 every day on ingredients
    fries_price = 12  # The price of French fries is $12
    poutine_price = 8  # The price of Poutine is $8
    fries_portion_cost = fries_price - daily_ingredient_cost  # Profit from a portion of French fries
    poutine_portion_cost = poutine_price - daily_ingredient_cost  # Profit from a portion of Poutine
    weekly_income = fries_portion_cost + poutine_portion_cost  # Lucius' weekly income

    # Calculate the tax Lucius has to pay
    tax = 0.1 * weekly_income

    # Calculate the income after paying the taxes and deducting the ingredient cost
    income_after_tax = (1 - 0.1) * weekly_income - (daily_ingredient_cost * 7)

    result = income_after_tax
    return result

print(solution())