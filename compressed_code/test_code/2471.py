def solution():
    
    laptop_price = 600
    smartphone_price = 400
    num_laptops = 2
    num_smartphones = 4
    total_cost = (laptop_price * num_laptops) + (smartphone_price * num_smartphones)
    change = 3000 - total_cost
    result = change
    return result

print(solution())