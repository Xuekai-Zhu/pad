def solution():
    total_spent = 50
    supplies_cost = 20
    num_skirts = 2
    
    # Subtract the cost of art supplies from the total spent to get the cost of both skirts
    skirt_cost = total_spent - supplies_cost
    
    # Divide the cost of both skirts by the number of skirts to get the cost of each skirt
    cost_per_skirt = skirt_cost / num_skirts
    result = cost_per_skirt
    return result

print(solution())