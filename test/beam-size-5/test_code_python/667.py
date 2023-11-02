def solution():
    
    type_a_candies = 7
    type_b_candies = 10
    type_a_price = 0.5
    type_b_price = 0.75
    total_cost = (type_a_candies * type_a_price) + (type_b_candies * type_b_price)
    change = 15 - total_cost
    result = change
    return result

print(solution())