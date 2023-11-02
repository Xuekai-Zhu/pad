def solution():
    # Define the prices of each fruit
    apple_price = 1
    orange_price = 2
    banana_price = 3

    # Calculate the total cost of each type of fruit that Mary wants to buy
    total_apple_cost = 5 * apple_price
    total_orange_cost = 3 * orange_price
    total_banana_cost = 2 * banana_price

    # Calculate the total cost before the discount
    total_cost_before_discount = total_apple_cost + total_orange_cost + total_banana_cost

    # Calculate the number of fruit that Mary bought
    total_fruit = 5 + 3 + 2

    # Calculate the number of $1 discounts Mary qualifies for
    discount_count = total_fruit // 5

    # Calculate the total discount Mary receives
    total_discount = discount_count * 1

    # Calculate the total cost after the discount
    total_cost_after_discount = total_cost_before_discount - total_discount

    result = total_cost_after_discount
    return result

print(solution())