def solution():
    # Calculate the number of customers in each week
    week_one_customers = 35
    week_two_customers = 2 * week_one_customers
    week_three_customers = 3 * week_one_customers

    # Calculate the total commission earned in three weeks
    total_commission = (week_one_customers + week_two_customers + week_three_customers) * 1

    # Calculate the total earnings, including commission and salary/bonus
    total_earnings = total_commission + 500 + 50
    result = total_earnings
    return result

print(solution())