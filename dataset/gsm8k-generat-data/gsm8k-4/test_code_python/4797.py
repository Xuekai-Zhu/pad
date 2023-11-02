def solution():
    """Zoe goes to the store to buy soda and pizza for herself and her 5 family members. Each bottle of soda costs half a dollar and each slice of pizza costs $1. Before she leaves her house she takes just enough money to pay for her purchase. How much money did Zoe take?"""
    # Define the number of people in Zoe's family and the cost of each item
    FAMILY_MEMBERS = 5
    SODA_COST = 0.5
    PIZZA_COST = 1

    # Calculate the total cost of the purchase
    total_cost = (FAMILY_MEMBERS + 1) * (SODA_COST + 2 * PIZZA_COST)

    # Return the total cost
    result = total_cost
    return result

print(solution())