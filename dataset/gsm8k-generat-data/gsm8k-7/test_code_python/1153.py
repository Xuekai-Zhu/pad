def solution():
    cleaning_cost = 150
    tip_percent = 0.1
    num_cleanings_per_month = 30/3
    chemical_cost_per_month = 200

    # Calculate the total cost of cleaning the pool
    total_cleaning_cost = (cleaning_cost * num_cleanings_per_month) * (1 + tip_percent)

    # Calculate the total monthly cost of the pool, including chemicals
    total_monthly_cost = total_cleaning_cost + chemical_cost_per_month
    result = total_monthly_cost
    return result

print(solution())