def solution():
    """Julio receives a $1 commission for every customer that buys in Edgars Fashion store. The store sells to 35 customers in the first week, twice as many in the second week, and triple as many as the first week in the third week. If he receives a salary of $500 for the 3 weeks and a bonus of $50, how much in total does he earn for the 3 weeks?"""
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