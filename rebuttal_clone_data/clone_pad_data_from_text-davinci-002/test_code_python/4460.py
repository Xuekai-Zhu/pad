def solution():
    vest_cost = 250
    weight_cost = 1.2 * 200
    weighted_vest_cost = 700
    discount = 100
    total_cost = vest_cost + weight_cost + weighted_vest_cost - discount
    result = total_cost
    return result

print(solution())