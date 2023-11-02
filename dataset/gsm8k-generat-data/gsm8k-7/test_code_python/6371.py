def solution():
    cash_register_cost = 1040
    bread_sales_per_day = 40
    bread_price = 2
    cake_sales_per_day = 6
    cake_price = 12
    rent_per_day = 20
    electricity_per_day = 2

    # Calculate the total profit per day
    total_sales_per_day = (bread_sales_per_day * bread_price) + (cake_sales_per_day * cake_price)
    total_expenses_per_day = rent_per_day + electricity_per_day
    total_profit_per_day = total_sales_per_day - total_expenses_per_day

    # Calculate the number of days needed to pay for the cash register
    days_to_pay = cash_register_cost / total_profit_per_day
    result = days_to_pay
    return result

print(solution())