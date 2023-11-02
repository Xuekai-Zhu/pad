def solution():
    """There are 30 pieces of popcorn in a serving. Jared can eat 90 pieces of popcorn and his three other friends can each eat 60 pieces of popcorn.
    How many servings of popcorn should Jared order for all of them?"""
    jared_pieces = 90
    friend_pieces = 60
    total_pieces = jared_pieces + (3 * friend_pieces)
    pieces_per_serving = 30
    servings_needed = total_pieces / pieces_per_serving
    result = servings_needed
    
    return result

print(solution())