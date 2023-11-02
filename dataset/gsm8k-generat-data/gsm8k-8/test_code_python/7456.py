def solution():
    # Define the cost of each fruit
    apple_cost = 1
    orange_cost = 2
    banana_cost = 3

    # Calculate the total cost before the discount
    total_cost_before_discount = (5 * apple_cost) + (3 * orange_cost) + (2 * banana_cost)

    # Calculate the number of fruit Mary bought
    num_fruit = 5 + 3 + 2

    # Calculate the number of discounts Mary gets
    num_discounts = num_fruit // 5

    # Calculate the total discount
    total_discount = num_discounts * 1

    # Calculate the total cost after the discount
    total_cost_after_discount = total_cost_before_discount - total_discount

    result = total_cost_after_discount
    return result

print(solution())