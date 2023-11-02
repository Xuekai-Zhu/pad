def solution():
    """Two hedgehogs found three baskets, each with 900 strawberries. The hedgehogs then each ate an equal number of strawberries. If 2/9 of the strawberries were remaining out of all the strawberries that were there, calculate the total number of strawberries that each hedgehog ate."""
    # Define the total number of strawberries in each basket
    strawberries_per_basket = 900

    # Define the total number of baskets found
    total_baskets = 3

    # Calculate the total number of strawberries before the hedgehogs ate
    total_strawberries = strawberries_per_basket * total_baskets

    # Calculate the fraction of strawberries remaining after the hedgehogs ate
    remaining_fraction = 2/9

    # Calculate the total number of strawberries eaten by both hedgehogs
    eaten_strawberries = total_strawberries - total_strawberries * remaining_fraction

    # Calculate the number of strawberries eaten by each hedgehog
    hedgehog_strawberries = eaten_strawberries / 2

    result = hedgehog_strawberries
    return result

print(solution())