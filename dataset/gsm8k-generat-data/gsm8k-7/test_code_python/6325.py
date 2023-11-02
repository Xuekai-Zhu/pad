def solution():
    num_mangoes = 6
    mango_price = 3

    num_apple_juice_cartons = 6
    apple_juice_price = 3

    total_cost = (num_mangoes * mango_price) + (num_apple_juice_cartons * apple_juice_price)
    amount_left = 50 - total_cost
    result = amount_left
    return result

print(solution())