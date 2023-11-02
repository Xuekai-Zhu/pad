def solution():
    
    commission_per_customer = 1
    first_week_customers = 35
    second_week_customers = first_week_customers * 2
    third_week_customers = first_week_customers * 3
    total_customers = first_week_customers + second_week_customers + third_week_customers
    total_commission = total_customers * commission_per_customer
    total_salary = 500
    bonus = 50
    total_earnings = total_commission + total_salary + bonus
    result = total_earnings
    return result

print(solution())