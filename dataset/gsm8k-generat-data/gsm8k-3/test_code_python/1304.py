def solution():
    """Julio receives a $1 commission for every customer that buys in Edgars Fashion Store. The store sells to 35 customers in the first week, twice as many in the second week, and triple as many as the first week in the third week. If he receives a salary of $500 for the 3 weeks and a bonus of $50, how much in total does he earn for the 3 weeks?"""
    # Define the commission rate and number of customers for each week
    COMMISSION_RATE = 1
    customers_1 = 35
    customers_2 = customers_1 * 2
    customers_3 = customers_1 * 3

    # Calculate the commission earned for each week
    commission_1 = customers_1 * COMMISSION_RATE
    commission_2 = customers_2 * COMMISSION_RATE
    commission_3 = customers_3 * COMMISSION_RATE

    # Calculate the total commission earned
    total_commission = commission_1 + commission_2 + commission_3

    # Calculate the total earnings (including salary and bonus)
    total_earnings = total_commission + 500 + 50

    # Display the total earnings
    result = total_earnings
    return result

print(solution())