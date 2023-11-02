def solution():
    """Henry drinks 15 bottles of kombucha every month.  Each bottle costs $3.00 and is eligible for a cash refund of $0.10 per bottle when he takes it to a recycling center.  After 1 year, how many bottles of kombucha will he be able to buy after he receives his cash refund?"""
    # Define the number of bottles of kombucha consumed per month and the cost per bottle
    BOTTLES_PER_MONTH = 15
    COST_PER_BOTTLE = 3.0

    # Define the cash refund per bottle and the number of months in a year
    CASH_REFUND_PER_BOTTLE = 0.1
    MONTHS_PER_YEAR = 12

    # Calculate the total number of bottles consumed in a year
    total_bottles = BOTTLES_PER_MONTH * MONTHS_PER_YEAR

    # Calculate the total cash refund received in a year
    cash_refund = total_bottles * CASH_REFUND_PER_BOTTLE

    # Calculate the total cost of the kombucha in a year
    total_cost = total_bottles * COST_PER_BOTTLE

    # Calculate the number of bottles Henry can buy after receiving the cash refund
    net_bottles = int((total_cost - cash_refund) / COST_PER_BOTTLE)

    # Display the number of bottles Henry can buy
    result = net_bottles
    return result

print(solution())