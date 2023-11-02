def solution():
    """Nate starts his camping trip with 70 matches. He drops 10 in a creek and his dog eats twice as many. How many matches does he have left?"""
    # Define the number of matches Nate started with
    starting_matches = 70

    # Define the number of matches Nate drops in the creek
    dropped_matches = 10

    # Define the number of matches Nate's dog eats
    dog_matches = dropped_matches * 2

    # Calculate the number of matches Nate has left
    remaining_matches = starting_matches - dropped_matches - dog_matches

    # Display the number of matches Nate has left
    result = remaining_matches
    return result

print(solution())