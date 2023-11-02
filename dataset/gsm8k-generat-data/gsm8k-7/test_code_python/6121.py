def solution():
    delta_price = 850
    delta_discount = 0.2  # 20% discount
    delta_price_with_discount = delta_price * (1 - delta_discount)

    united_price = 1100
    united_discount = 0.3  # 30% discount
    united_price_with_discount = united_price * (1 - united_discount)

    # Compare the prices of the two flights and get the cheaper price
    cheaper_price = min(delta_price_with_discount, united_price_with_discount)

    # Calculate the amount of money that can be saved by choosing the cheaper flight
    delta_savings = delta_price_with_discount - cheaper_price
    united_savings = united_price_with_discount - cheaper_price
    total_savings = delta_savings + united_savings
    result = total_savings
    return result

print(solution())