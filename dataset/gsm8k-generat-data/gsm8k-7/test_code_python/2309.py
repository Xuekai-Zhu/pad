def solution():
    num_employees = 20
    num_shirts_per_employee_per_day = 20
    working_hours_per_day = 8
    hourly_wage = 12
    payment_per_shirt = 5
    selling_price_per_shirt = 35
    nonemployee_expenses_per_day = 1000

    # Calculate the total number of shirts produced per day
    total_shirts_per_day = num_employees * num_shirts_per_employee_per_day

    # Calculate the total cost of labor per day
    total_labor_cost_per_day = num_employees * working_hours_per_day * hourly_wage

    # Calculate the total payment per day for shirts produced
    total_shirt_payment_per_day = total_shirts_per_day * payment_per_shirt

    # Calculate the total revenue per day from selling shirts
    total_revenue_per_day = total_shirts_per_day * selling_price_per_shirt

    # Calculate the total profit per day
    total_profit_per_day = total_revenue_per_day - total_labor_cost_per_day - total_shirt_payment_per_day - nonemployee_expenses_per_day
    result = total_profit_per_day
    return result

print(solution())