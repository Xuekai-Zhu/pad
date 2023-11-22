def solution():
    
    # Define the initial cost of filling up 20 helium balloons and the cost increase per balloon
    INITIAL_COST = 900
    COST_INCREASE = 20

    # Calculate the cost of filling up 170 helium balloons after the price increase
    new_cost = INITIAL_COST + (COST_INCREASE * 20)

    # Calculate the total cost of filling up 170 helium balloons
    total_cost = new_cost * 170

    # Display the total cost
    result = total_cost
    return result

print(solution())