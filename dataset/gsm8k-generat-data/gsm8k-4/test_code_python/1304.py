def solution():
    """Julio receives a $1 commission for every customer that buys in Edgars Fashion Store. The store sells to 35 customers in the first week, twice as many in the second week, and triple as many as the first week in the third week. If he receives a salary of $500 for the 3 weeks and a bonus of $50, how much in total does he earn for the 3 weeks?"""
    # Define the commission rate and the number of customers in each week
    commission_rate = 1
    customers_week1 = 35
    customers_week2 = customers_week1 * 2
    customers_week3 = customers_week1 * 3

    # Calculate the total commission earned
    commission_earned = commission_rate * (customers_week1 + customers_week2 + customers_week3)

    # Calculate the total earnings including salary and bonus
    total_earnings = commission_earned + 500 + 50

    result = total_earnings
    return result

print(solution())