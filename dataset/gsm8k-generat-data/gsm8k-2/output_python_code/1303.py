def solution():
    """Julio receives a $1 commission for every customer that buys in Edgars Fashion Store. The store sells to 35 customers in the first week, twice as many in the second week, and triple as many as the first week in the third week. If he receives a salary of $500 for the 3 weeks and a bonus of $50, how much in total does he earn for the 3 weeks?"""
    first_week_sales = 35
    second_week_sales = first_week_sales * 2
    third_week_sales = first_week_sales * 3
    total_sales = first_week_sales + second_week_sales + third_week_sales
    commission = total_sales * 1
    salary = 500
    bonus = 50
    total_earnings = commission + salary + bonus
    result = total_earnings
    return result

print(solution())