def solution():
    """Two hedgehogs found three baskets, each with 900 strawberries. The hedgehogs then each ate an equal number of strawberries. If 2/9 of the strawberries were remaining out of all the strawberries that were there, calculate the total number of strawberries that each hedgehog ate."""
    total_strawberries = 3 * 900
    remaining_strawberries = total_strawberries * (2/9)
    eaten_strawberries = total_strawberries - remaining_strawberries
    strawberries_per_hedgehog = eaten_strawberries / 2
    result = strawberries_per_hedgehog
    return result

print(solution())