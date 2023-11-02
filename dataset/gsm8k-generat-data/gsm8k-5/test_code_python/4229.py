def solution():
    starting_matches = 70  # Nate starts with 70 matches
    lost_matches = 10  # He drops 10 in a creek
    dog_matches = lost_matches * 2  # His dog eats twice as many
    remaining_matches = starting_matches - lost_matches - dog_matches  # Calculate the remaining matches

    result = remaining_matches
    return result

print(solution())