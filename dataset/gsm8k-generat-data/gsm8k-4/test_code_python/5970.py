def solution():
    """There are 30 pieces of popcorn in a serving. Jared can eat 90 pieces of popcorn and his three other friends can each eat 60 pieces of popcorn. How many servings of popcorn should Jared order for all of them?"""
    # Define the number of pieces of popcorn in a serving
    pieces_per_serving = 30

    # Define the number of pieces of popcorn Jared can eat
    jared_pieces = 90

    # Define the number of pieces of popcorn each of Jared's friends can eat
    friend_pieces = 60

    # Calculate the total number of pieces of popcorn that everyone can eat
    total_pieces = jared_pieces + (3 * friend_pieces)

    # Calculate the number of servings needed
    servings_needed = total_pieces // pieces_per_serving

    # Add one extra serving if there are leftovers
    if total_pieces % pieces_per_serving != 0:
        servings_needed += 1

    result = servings_needed
    return result

print(solution())