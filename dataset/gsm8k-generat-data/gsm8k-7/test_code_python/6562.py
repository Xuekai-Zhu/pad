def solution():
    pretzel_price = 4
    chip_price = pretzel_price * 1.75
    num_chips = 2
    num_pretzels = 2
    
    # Calculate the total cost of all chips
    total_chip_cost = chip_price * num_chips
    
    # Calculate the total cost of all pretzels
    total_pretzel_cost = pretzel_price * num_pretzels
    
    # Calculate the total cost of all purchases
    total_cost = total_chip_cost + total_pretzel_cost
    result = total_cost
    return result

print(solution())