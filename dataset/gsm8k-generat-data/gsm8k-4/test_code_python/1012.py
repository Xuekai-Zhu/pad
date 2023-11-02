def solution():
    """Brian is a real estate agent. He makes a 2% commission on each sale. During June, he sold three houses. The houses sold for $157,000, $499,000, and $125,000. What was Brian’s total commission on these three sales?"""
    # Define the commission rate
    commission_rate = 0.02

    # Define the sale prices of the three houses
    sale_price_1 = 157000
    sale_price_2 = 499000
    sale_price_3 = 125000

    # Calculate the commission earned on each sale
    commission_1 = sale_price_1 * commission_rate
    commission_2 = sale_price_2 * commission_rate
    commission_3 = sale_price_3 * commission_rate

    # Calculate the total commission earned
    total_commission = commission_1 + commission_2 + commission_3
    result = total_commission
    return result

print(solution())