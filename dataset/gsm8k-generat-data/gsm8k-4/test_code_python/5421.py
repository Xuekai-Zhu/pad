def solution():
    """Hannah is at a restaurant. She spends $23 in total on an entree and a dessert. If the entree costs $5 more than the dessert, how much does the entree cost, in dollars?"""
    # Define the total amount spent
    total_spent = 23

    # Define the cost difference between the entree and dessert
    cost_difference = 5

    # Set up the equation
    # entree_cost + dessert_cost = total_spent
    # entree_cost = dessert_cost + cost_difference
    # Substitute the second equation into the first
    # dessert_cost + cost_difference + dessert_cost = total_spent
    # Simplify
    # 2*dessert_cost + cost_difference = total_spent
    # Solve for dessert_cost
    dessert_cost = (total_spent - cost_difference) / 2

    # Calculate the cost of the entree
    entree_cost = dessert_cost + cost_difference

    # Return the result
    result = entree_cost
    return result

print(solution())