def solution():
    # Calculate the total cost of the groceries
    milk_price = 4.00/2  # milk is 1/2 off today
    bananas_price = 0.75 * 2
    total_cost = milk_price + 3.50 + 10.25 - 1.25 + bananas_price  # taking into account the coupon

    # Calculate the amount of money left over after buying the groceries
    money_left_over = 20 - total_cost
    result = money_left_over
    return result

print(solution())