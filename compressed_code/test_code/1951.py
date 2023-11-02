def solution():
    
    total_value = 20000
    diamond_earring_cost = 6000
    iphone_cost = 2000
    scarf_cost = 1500
    num_diamond_earrings = 2
    num_scarves = (total_value - (num_diamond_earrings * diamond_earring_cost) - iphone_cost) / scarf_cost
    result = num_scarves
    return result

print(solution())