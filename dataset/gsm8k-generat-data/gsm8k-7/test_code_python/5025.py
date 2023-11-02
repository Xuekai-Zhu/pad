def solution():
    # First applicant calculations
    first_salary = 42000
    first_revenue = 93000
    first_training_months = 3
    first_training_cost = 1200

    first_total_cost = first_salary + (first_training_months * first_training_cost)
    first_profit = first_revenue - first_total_cost

    # Second applicant calculations
    second_salary = 45000
    second_bonus_percent = 0.01
    second_revenue = 92000

    second_total_cost = second_salary + (second_salary * second_bonus_percent)
    second_profit = second_revenue - second_total_cost

    # Calculate the difference in profit between the two applicants
    profit_difference = abs(first_profit - second_profit)
    result = profit_difference
    return result

print(solution())