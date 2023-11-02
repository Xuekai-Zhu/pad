def solution():
    """Jerry had 63 pieces of candy.  He divided them up equally into 9 bags.  2 of the bags had chocolate hearts.  3 of the bags were chocolate kisses.  The rest of the bags were not chocolate.  How many pieces of candy were not chocolate?"""
    # Divide the 63 pieces of candy equally into 9 bags
    candy_per_bag = 63 // 9

    # Calculate the total number of chocolate hearts
    chocolate_hearts = 2 * candy_per_bag

    # Calculate the total number of chocolate kisses
    chocolate_kisses = 3 * candy_per_bag

    # Calculate the total number of non-chocolate candies
    non_chocolate = 63 - (chocolate_hearts + chocolate_kisses)

    # Display the number of non-chocolate candies
    result = non_chocolate
    return result

print(solution())