def solution():
    """Brian is a real estate agent. He makes a 2% commission on each sale. During June, he sold three houses. The houses sold for $157,000, $499,000, and $125,000. What was Brian’s total commission on these three sales?"""
    # Define Brian's commission rate
    COMMISSION_RATE = 0.02

    # Define the sale prices of the three houses
    sale_price1 = 157000
    sale_price2 = 499000
    sale_price3 = 125000

    # Calculate Brian's commission on each sale
    commission1 = sale_price1 * COMMISSION_RATE
    commission2 = sale_price2 * COMMISSION_RATE
    commission3 = sale_price3 * COMMISSION_RATE

    # Calculate Brian's total commission on the three sales
    total_commission = commission1 + commission2 + commission3

    # Display Brian's total commission
    result = total_commission
    return result

print(solution())