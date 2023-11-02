def solution():
    sale_prices = [157000, 499000, 125000]  # Sale prices of the three houses
    commission_rate = 0.02  # Brian makes a 2% commission on each sale

    # Calculate the commission earned on each sale
    commissions = [sale_price * commission_rate for sale_price in sale_prices]

    # Calculate the total commission earned
    total_commission = sum(commissions)
    result = total_commission
    return result

print(solution())