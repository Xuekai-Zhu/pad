def solution():
    
    # Define the cost of the bedroom set and the cost of the old bedroom
    bedroom_cost = 3000
    old_bedroom_cost = 1000

    # Calculate the cost of the bedroom set after paying for the old bedroom
    bedroom_cost_after_purchase = bedroom_cost - old_bedroom_cost

    # Calculate the cost per month
    monthly_cost = bedroom_cost_after_purchase * 0.1

    # Display the cost per month
    result = monthly_cost
    return result

print(solution())