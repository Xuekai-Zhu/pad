def solution():
    price_per_sunglasses = 30  # Sunglasses are sold for $30 each
    pairs_sold_per_day = 10  # Vendor sells 10 pairs of sunglasses per day
    cost_of_new_sign = 20  # Half of the profits are used to buy a new sign that costs $20 

    # Calculate the total amount earned from selling 10 pairs of sunglasses in a day
    total_earnings = price_per_sunglasses * pairs_sold_per_day

    # Calculate the total profit after deducting the cost of buying the sunglasses
    total_profit = total_earnings - cost_of_new_sign

    # Calculate the cost of each pair of sunglasses to the vendor
    cost_per_sunglasses = total_profit / pairs_sold_per_day
    result = cost_per_sunglasses
    return result

print(solution())