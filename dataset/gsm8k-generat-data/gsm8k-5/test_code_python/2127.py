def solution():
    price_A = 125  # Store A lists the smartphone for $125
    discount_A = 0.08  # Store A offers an 8% discount
    price_B = 130  # Store B lists the smartphone for $130
    discount_B = 0.1  # Store B offers a 10% discount

    # Calculate the final price for each store's smartphone
    final_price_A = price_A * (1 - discount_A)
    final_price_B = price_B * (1 - discount_B)

    # Calculate how much cheaper Store A's smartphone is compared to Store B's smartphone
    difference = final_price_B - final_price_A
    result = difference
    return result

print(solution())