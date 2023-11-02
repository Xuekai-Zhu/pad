def solution():
    num_bread = 1
    bread_price = 4.0

    num_meat_packs = num_bread * 2
    meat_price = 5.0
    meat_coupon = 1.0

    num_cheese_packs = num_bread * 2
    cheese_price = 4.0
    cheese_coupon = 1.0

    # Calculate the total cost of ingredients
    total_cost = (num_bread * bread_price) + (num_meat_packs * (meat_price - meat_coupon)) + (num_cheese_packs * (cheese_price - cheese_coupon))

    # Calculate the number of sandwiches that can be made with the ingredients
    num_sandwiches = num_bread * 10

    # Calculate the cost per sandwich
    cost_per_sandwich = total_cost / num_sandwiches
    result = cost_per_sandwich
    return result

print(solution())