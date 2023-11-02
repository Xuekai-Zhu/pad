def solution():
    """Brian is a real estate agent. He makes a 2% commission on each sale. During June, he sold three houses. The houses sold for $157,000, $499,000, and $125,000. What was Brian’s total commission on these three sales?"""
    sale_prices = [157000, 499000, 125000]
    commission_rate = 0.02
    total_commission = sum([sale_price * commission_rate for sale_price in sale_prices])
    result = total_commission
    return result

print(solution())