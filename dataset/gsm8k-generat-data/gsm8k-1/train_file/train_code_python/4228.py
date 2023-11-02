def solution():
    """Nate starts his camping trip with 70 matches. He drops 10 in a creek and his dog eats twice as many. How many matches does he have left?"""
    starting_matches = 70
    matches_dropped = 10
    matches_eaten_by_dog = matches_dropped * 2
    remaining_matches = starting_matches - matches_dropped - matches_eaten_by_dog
    result = remaining_matches
    return result

print(solution())