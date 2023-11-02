def solution():
    discount = 10
    additional_discount = 4
    number_of_children = 4
    total_discount = discount + additional_discount
    cost_of_shoes = 125
    final_cost = cost_of_shoes - (cost_of_shoes * (total_discount / 100))
    result = final_cost
    
    return result

print(solution())