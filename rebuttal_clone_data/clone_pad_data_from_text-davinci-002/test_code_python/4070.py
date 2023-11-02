def solution():
    daily_ingredient_cost = 10
    weekly_ingredient_cost = daily_ingredient_cost * 7
    price_french_fries = 12
    price_poutine = 8
    number_of_french_fries_sold = 20
    number_of_poutine_sold = 10
    total_sales = (price_french_fries * number_of_french_fries_sold) + (price_poutine * number_of_poutine_sold)
    tax_rate = 10
    tax_amount = total_sales * (tax_rate / 100)
    weekly_income = total_sales - tax_amount
    weekly_expenses = weekly_ingredient_cost
    result = weekly_income - weekly_expenses
    return result

print(solution())