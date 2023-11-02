def solution():
    # Calculate the total number of strawberries in the baskets
    total_strawberries = 3 * 900

    # Calculate the number of strawberries remaining after the hedgehogs ate
    remaining_strawberries = total_strawberries * (2/9)

    # Calculate the number of strawberries each hedgehog ate
    each_hedgehog = (total_strawberries - remaining_strawberries) / 2
    result = each_hedgehog
    return result

print(solution())