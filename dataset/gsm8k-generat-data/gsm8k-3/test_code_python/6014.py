def solution():
    """Sean buys 3 cans of soda, 2 soups, and 1 sandwich. Each soup costs as much as the 3 combined sodas. The sandwich cost 3 times as much as the soup. If the soda costs $1, how much did everything cost together?"""
    # Define the cost of a soda
    SODA_COST = 1

    # Calculate the cost of the soups based on the cost of the sodas
    SOUP_COST = SODA_COST * 3

    # Calculate the cost of the sandwich based on the cost of the soup
    SANDWICH_COST = SOUP_COST * 3

    # Calculate the total cost of the purchase
    total_cost = (3 * SODA_COST) + (2 * SOUP_COST) + SANDWICH_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())