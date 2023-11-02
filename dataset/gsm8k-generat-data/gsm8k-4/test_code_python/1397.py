def solution():
    """Marly is making soup. He adds 2 quarts of milk and three times as much chicken stock to 1 quart of pureed vegetables. Then he divides the soup into bags that can hold 3 quarts each. How many bags does he need?"""
    # Define the amount of milk and pureed vegetables
    milk = 2
    vegetables = 1

    # Calculate the amount of chicken stock
    chicken_stock = 3 * vegetables

    # Calculate the total amount of soup
    total_soup = milk + chicken_stock + vegetables

    # Calculate the number of bags needed, rounding up to the nearest integer
    bags_needed = (total_soup + 2) // 3

    # Return the result
    result = bags_needed
    return result

print(solution())