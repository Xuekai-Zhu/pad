def solution():
    cost_per_month = 80
    percent_to_pay = 0.4  # 40% of the cost

    # Calculate the cost that Nancy will pay each month
    nancy_paid_per_month = cost_per_month * percent_to_pay

    # Calculate the total cost that Nancy will pay in one year
    nancy_paid_per_year = nancy_paid_per_month * 12
    result = nancy_paid_per_year
    return result

print(solution())