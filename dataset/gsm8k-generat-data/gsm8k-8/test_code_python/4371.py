def solution():
    # Calculate the total number of pieces of candy in each bag
    candy_per_bag = 63 / 9

    # Calculate the number of chocolate hearts
    chocolate_hearts = 2 * candy_per_bag

    # Calculate the number of chocolate kisses
    chocolate_kisses = 3 * candy_per_bag

    # Calculate the total number of chocolate pieces
    total_chocolate = chocolate_hearts + chocolate_kisses

    # Calculate the number of pieces of candy that were not chocolate
    not_chocolate = 63 - total_chocolate
    result = not_chocolate
    return result

print(solution())