def solution():
    
    meat_cost = 5.00
    crackers_cost = 3.50
    vegetables_cost = 2.00 * 4
    cheese_cost = 3.50
    total_cost = meat_cost + crackers_cost + vegetables_cost + cheese_cost
    discount = total_cost * 0.10
    final_cost = total_cost - discount
    result = final_cost
    return result

print(solution())