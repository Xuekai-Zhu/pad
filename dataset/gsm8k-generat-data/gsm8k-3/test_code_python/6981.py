def solution():
    """Boris has 100 pieces of Halloween candy. His daughter eats 8 pieces of candy. He separates the remaining pieces of candy into equal portions into 4 different bowls. Then he takes away 3 pieces of candy from each bowl to keep for himself. How many pieces of candy are in one bowl?"""
    # Define the starting number of candy pieces
    STARTING_CANDY = 100

    # Subtract the amount his daughter eats
    candy_left = STARTING_CANDY - 8

    # Divide the remaining candy into 4 equal portions
    candy_per_bowl = candy_left / 4

    # Subtract 3 pieces of candy from each bowl
    candy_per_bowl -= 3

    # Display the number of pieces of candy in one bowl
    result = candy_per_bowl
    return result

print(solution())