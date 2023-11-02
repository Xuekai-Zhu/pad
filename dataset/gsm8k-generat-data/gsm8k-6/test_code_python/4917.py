def solution():
    # Calculate the number of crates needed to ship 540 pounds of fish
    num_crates = 540 // 30  

    # Calculate the cost of shipping all the crates
    shipping_cost = num_crates * 1.5 
    result = shipping_cost
    return result

print(solution())