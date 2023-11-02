def solution():
    first_month_savings = 10
    monthly_increase = 30
    months_saved = 3

    # Calculate the total savings after three months
    total_savings = first_month_savings + (monthly_increase * (months_saved - 1))

    result = total_savings
    return result

print(solution())