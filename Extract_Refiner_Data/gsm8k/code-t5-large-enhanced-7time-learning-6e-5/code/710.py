def solution():
    
    # Define the cost of picking and buying blueberries per pound
    COST_PER_POUND = 1.5

    # Define the number of pounds of blueberries picked
    pounds_picked = 30

    # Calculate the total cost of picking blueberries
    total_cost = 20 + (pounds_picked * COST_PER_POUND)

    # Calculate the cost of buying the blueberries at the store
    store_cost = 2.5 * pounds_picked

    # Calculate the savings
    savings = total_cost - store_cost

    # Display the savings
    result = savings
    return result

print(solution())