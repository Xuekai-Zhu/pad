def solution():
    initial_money = 500
    potatoes_price = 2
    potatoes_weight = 6
    tomato_price = 3
    tomato_weight = 9
    cucumber_price = 4
    cucumber_weight = 5
    bananas_price = 5
    bananas_weight = 3

    # Calculate the total cost of all items
    total_cost = (potatoes_price * potatoes_weight) + (tomato_price * tomato_weight) + \
                 (cucumber_price * cucumber_weight) + (bananas_price * bananas_weight)

    # Calculate Peter's remaining money
    remaining_money = initial_money - total_cost
    result = remaining_money
    return result

print(solution())