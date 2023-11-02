def solution():
    apples_per_pack = 10
    apples_pack_price = 2
    oranges_per_pack = 5
    oranges_pack_price = 1.5
    num_fruits_to_buy = 12

    # Calculate the price per apple and per orange
    apple_price = apples_pack_price / apples_per_pack
    orange_price = oranges_pack_price / oranges_per_pack

    # Determine which fruit is cheaper
    if apple_price <= orange_price:
        cheaper_fruit_price = apple_price
    else:
        cheaper_fruit_price = orange_price

    # Calculate the total cost of buying 12 of the cheaper fruit
    total_cost = cheaper_fruit_price * num_fruits_to_buy * 100
    result = int(total_cost)  # express result in cents (as an integer)
    return result

print(solution())