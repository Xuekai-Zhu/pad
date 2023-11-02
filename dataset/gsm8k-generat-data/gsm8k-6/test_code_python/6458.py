def solution():
    # Calculate the cost of buns
    cost_of_buns = 10 * 0.1  

    # Calculate the cost of milk
    cost_of_milk = 2 * 2  

    # Calculate the cost of one bottle of milk
    cost_of_one_bottle_of_milk = cost_of_milk / 2  

    # Calculate the cost of the carton of eggs
    cost_of_carton_of_eggs = 3 * cost_of_one_bottle_of_milk  

    # Calculate the total cost
    total_cost = cost_of_buns + cost_of_milk + cost_of_carton_of_eggs  
    result = total_cost
    return result

print(solution())