def solution():
    gallon_cost = 8  # 1 gallon of mayo at Costco costs $8
    normal_price = 3  # 1 16-ounce bottle at the normal store costs $3
    normal_volume = 128  # There are 128 ounces in 1 gallon

    # Calculate the cost of buying the same amount of mayo at the normal store
    normal_cost = (normal_volume / 16) * normal_price

    # Calculate the amount of money saved by buying in bulk
    saved_money = normal_cost - gallon_cost
    result = saved_money
    return result

print(solution())