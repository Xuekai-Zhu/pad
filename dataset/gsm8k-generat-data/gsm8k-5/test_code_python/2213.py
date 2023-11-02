def solution():
    cost_per_month = 80
    percentage = 0.4
    months_per_year = 12

    # Calculate the total cost per year
    total_cost = cost_per_month * months_per_year

    # Calculate the amount Nancy will pay each year
    amount_to_pay = total_cost * percentage
    result = amount_to_pay
    return result

print(solution())