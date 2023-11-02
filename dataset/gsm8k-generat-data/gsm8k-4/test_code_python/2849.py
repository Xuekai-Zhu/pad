def solution():
    """For breakfast, Anna bought a bagel for $0.95 and a glass of orange juice for $0.85. At lunch, Anna spent $4.65 on a sandwich and $1.15 on a carton of milk. How much more money did Anna spend on lunch than on breakfast?"""
    # Define the prices of breakfast items
    bagel_price = 0.95
    juice_price = 0.85

    # Define the prices of lunch items
    sandwich_price = 4.65
    milk_price = 1.15

    # Calculate the total cost of breakfast
    breakfast_cost = bagel_price + juice_price

    # Calculate the total cost of lunch
    lunch_cost = sandwich_price + milk_price

    # Calculate the difference in cost between lunch and breakfast
    cost_difference = lunch_cost - breakfast_cost

    # Return the result
    result = cost_difference
    return result

print(solution())