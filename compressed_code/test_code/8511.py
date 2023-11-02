def solution():
    
    starting_money = 20
    milk_cost = 4
    bread_cost = 3.5
    detergent_cost = 10.25
    banana_cost = 0.75
    banana_weight = 2
    detergent_coupon = 1.25
    milk_discount = milk_cost / 2
    total_cost = milk_discount + bread_cost + detergent_cost - detergent_coupon + (banana_cost * banana_weight)
    leftover_money = starting_money - total_cost
    result = leftover_money
    return result

print(solution())