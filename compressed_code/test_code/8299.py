def solution():
    
    num_laptops = 2
    laptop_cost = 600
    num_smartphones = 4
    smartphone_cost = 400
    total_cost = (num_laptops * laptop_cost) + (num_smartphones * smartphone_cost)
    change = 3000 - total_cost
    result = change
    
    return result

print(solution())