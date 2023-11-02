def solution():
    """Nate starts his camping trip with 70 matches. He drops 10 in a creek and his dog eats twice as many. How many matches does he have left?"""
    starting_matches = 70
    dropped_matches = 10
    dog_matches = 2 * dropped_matches
    remaining_matches = starting_matches - dropped_matches - dog_matches
    result = remaining_matches
    return result

print(solution())