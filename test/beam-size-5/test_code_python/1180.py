def solution():
    
    # Define the amount of coal ordered and the cost per unit
    coal_ordered = 850
    cost_per_bag = 18

    # Calculate the number of bags of coal ordered
    bags_ordered = coal_ordered / 50

    # Calculate the total cost of the order
    total_cost = bags_ordered * cost_per_bag

    # Display the total cost
    result = total_cost
    return result

print(solution())