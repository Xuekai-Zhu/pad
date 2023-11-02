def solution():
    customers_week_1 = 35
    customers_week_2 = customers_week_1 * 2
    customers_week_3 = customers_week_1 * 3
    commission_week_1 = customers_week_1 * 1
    commission_week_2 = customers_week_2 * 1
    commission_week_3 = customers_week_3 * 1
    total_commission = commission_week_1 + commission_week_2 + commission_week_3
    salary = 500
    bonus = 50
    total_earnings = total_commission + salary + bonus
 
    return result

print(solution())