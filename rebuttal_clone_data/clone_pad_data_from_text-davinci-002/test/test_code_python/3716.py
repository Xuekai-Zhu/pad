def solution():
    number_of_toys = 5
    cost_per_toy = 3
    discount = 20
    total_cost = number_of_toys * cost_per_toy
    total_discount = total_cost * (discount / 100)
    final_cost = total_cost - total_discount
    result = final_cost
    
    return result

print(solution())