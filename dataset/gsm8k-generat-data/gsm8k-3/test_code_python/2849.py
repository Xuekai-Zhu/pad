def solution():
    """For breakfast, Anna bought a bagel for $0.95 and a glass of orange juice for $0.85. At lunch, Anna spent $4.65 on a sandwich and $1.15 on a carton of milk. How much more money did Anna spend on lunch than on breakfast?"""
    # Define the cost of each item
    BAGEL_COST = 0.95
    JUICE_COST = 0.85
    SANDWICH_COST = 4.65
    MILK_COST = 1.15

    # Calculate the total cost of breakfast
    breakfast_cost = BAGEL_COST + JUICE_COST

    # Calculate the total cost of lunch
    lunch_cost = SANDWICH_COST + MILK_COST

    # Calculate the difference in cost between lunch and breakfast
    difference = lunch_cost - breakfast_cost

    # Display the difference in cost
    result = difference
    return result

print(solution())