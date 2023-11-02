def solution():
    # Define the cost of one candy bar
    candy_cost = 1.5
    
    # Define the cost of one pack of gum
    gum_cost = candy_cost / 2
    
    # Calculate the total cost of the candy bars
    candy_total_cost = 3 * candy_cost
    
    # Calculate the total cost of the gum
    gum_total_cost = 2 * gum_cost
    
    # Calculate the total cost of both purchases
    total_cost = candy_total_cost + gum_total_cost
    result = total_cost
    return result

print(solution())