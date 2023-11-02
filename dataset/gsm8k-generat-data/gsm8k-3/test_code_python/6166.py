def solution():
    """Two hedgehogs found three baskets, each with 900 strawberries. The hedgehogs then each ate an equal number of strawberries. If 2/9 of the strawberries were remaining out of all the strawberries that were there, calculate the total number of strawberries that each hedgehog ate."""
    # Define the number of baskets and strawberries per basket
    BASKETS = 3
    STRAWBERRIES_PER_BASKET = 900

    # Calculate the total number of strawberries
    total_strawberries = BASKETS * STRAWBERRIES_PER_BASKET

    # Determine how many strawberries each hedgehog ate
    remaining_strawberries = total_strawberries * (2/9)
    ate_strawberries = (total_strawberries - remaining_strawberries) / 2

    # Display the number of strawberries each hedgehog ate
    result = ate_strawberries
    return result

print(solution())