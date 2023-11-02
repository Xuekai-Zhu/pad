def solution():
    """Nate starts his camping trip with 70 matches. He drops 10 in a creek and his dog eats twice as many. How many matches does he have left?"""
    # Define the starting number of matches
    starting_matches = 70

    # Define the number of matches dropped in the creek
    creek_matches = 10

    # Define the number of matches eaten by the dog
    dog_matches = 2 * creek_matches

    # Calculate the number of matches remaining
    remaining_matches = starting_matches - creek_matches - dog_matches

    # Return the result
    result = remaining_matches
    return result

print(solution())