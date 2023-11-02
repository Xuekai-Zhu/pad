def solution():
    total_cost = 110
    cost_of_coat = 40
    cost_of_shoes = 30
    cost_of_jeans = total_cost - cost_of_coat - cost_of_shoes
    price_of_one_pair = cost_of_jeans / 2
    result = price_of_one_pair
    return result

print(solution())