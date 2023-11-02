def solution():
    """Hannah is at a restaurant. She spends $23 in total on an entree and a dessert. If the entree costs $5 more than the dessert, how much does the entree cost, in dollars?"""
    # Define the difference in cost between the entree and the dessert
    ENTREE_DESSERT_DIFFERENCE = 5

    # Define the total amount spent
    total_spent = 23

    # Calculate the cost of the dessert
    dessert_cost = (total_spent - ENTREE_DESSERT_DIFFERENCE) / 2

    # Calculate the cost of the entree
    entree_cost = dessert_cost + ENTREE_DESSERT_DIFFERENCE

    # Display the cost of the entree
    result = entree_cost
    return result

print(solution())