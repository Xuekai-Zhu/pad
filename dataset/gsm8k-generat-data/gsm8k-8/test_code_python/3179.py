def solution():
    laptop_cost = 600
    smartphone_cost = 400
    num_laptops = 2
    num_smartphones = 4
    total_cost = laptop_cost * num_laptops + smartphone_cost * num_smartphones
    change = 3000 - total_cost
    result = change
    return result

print(solution())