def solution():
    # Calculate the total number of strawberries before the hedgehogs ate
    total_strawberries = 3 * 900  # each basket had 900 strawberries

    # Calculate the number of strawberries remaining after the hedgehogs ate
    remaining_strawberries = (2/9) * total_strawberries

    # Calculate the number of strawberries eaten by each hedgehog (assuming they ate an equal amount)
    eaten_strawberries = (total_strawberries - remaining_strawberries) / 2

    result = eaten_strawberries
    return result

print(solution())