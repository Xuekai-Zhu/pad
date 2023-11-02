def solution():
    """Joe sells ham and cheese sandwiches for $1.50. If a slice of bread costs $0.15, a slice of ham costs $0.25 and a slice of cheese costs $0.35, how many cents does a sandwich with one slice of each protein cost Joe to make?"""
    # Define the cost of each component
    BREAD_COST = 0.15
    HAM_COST = 0.25
    CHEESE_COST = 0.35

    # Calculate the total cost of one sandwich
    total_cost = BREAD_COST + HAM_COST + CHEESE_COST

    # Convert the total cost to cents
    cost_in_cents = total_cost * 100

    # Display the cost in cents
    result = cost_in_cents
    return result

print(solution())