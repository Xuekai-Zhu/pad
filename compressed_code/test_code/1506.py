def solution():
    
    individual_cost = 10
    discount = 0.1
    
    individual_total_cost = 3 * individual_cost
    
    discount_total_cost = individual_total_cost - (individual_total_cost * discount)
    
    savings = individual_total_cost - discount_total_cost
    result = savings
    return result

print(solution())