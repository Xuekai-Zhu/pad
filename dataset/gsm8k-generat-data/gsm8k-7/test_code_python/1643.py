def solution():
    num_small_bulbs = 3
    small_bulb_price = 8

    num_large_bulbs = 1
    large_bulb_price = 12

    total_cost = (num_small_bulbs * small_bulb_price) + (num_large_bulbs * large_bulb_price)
    money_left = 60 - total_cost
    result = money_left
    return result

print(solution())