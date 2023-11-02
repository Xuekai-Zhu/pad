def solution():
    # Calculate the discounted price of each bag
    discounted_price = 6.00 * 0.25  # 75% off is the same as 25% of the original price
    bag_price = 6.00 - discounted_price  # final price of each bag after discount
    # Calculate the total cost of two bags
    total_cost = bag_price * 2
    result = total_cost
    return result

print(solution())