def solution():
    first_week_customers = 35
    second_week_customers = first_week_customers * 2
    third_week_customers = first_week_customers * 3
    commission_per_customer = 1
    salary = 500
    bonus = 50

    # Calculate the total commission earned
    total_customers = first_week_customers + second_week_customers + third_week_customers
    total_commission = total_customers * commission_per_customer

    # Calculate the total earnings
    total_earnings = total_commission + salary + bonus
    result = total_earnings
    return result

print(solution())