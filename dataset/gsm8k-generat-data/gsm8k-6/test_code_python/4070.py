def solution():
    # Calculate the total cost of ingredients for a week
    ingredient_cost = 10 * 7 # $10 spent every day for 7 days

    # Calculate the total revenue from selling French fries and Poutine
    french_fries_revenue = 12 * 7 # $12 per portion and selling for 7 days
    poutine_revenue = 8 * 7 # $8 per portion and selling for 7 days
    total_revenue = french_fries_revenue + poutine_revenue

    # Calculate the amount of tax Lucius needs to pay
    tax = total_revenue * 0.1

    # Calculate Lucius' profit for the week
    profit = total_revenue - ingredient_cost - tax
    result = profit
    return result

print(solution())