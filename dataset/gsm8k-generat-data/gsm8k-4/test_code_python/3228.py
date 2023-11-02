def solution():
    """For breakfast, Daisy bought a muffin for $2 and a cup of coffee for $4. For lunch, Daisy had soup, a salad, and lemonade. The soup cost $3, the salad cost $5.25, and the lemonade cost $0.75. How much more money did Daisy spend on lunch than on breakfast?"""
    # Define the cost of breakfast and lunch
    breakfast_cost = 2 + 4
    lunch_cost = 3 + 5.25 + 0.75

    # Calculate the difference in cost between lunch and breakfast
    difference = lunch_cost - breakfast_cost

    # Return the result
    result = difference
    return result

print(solution())