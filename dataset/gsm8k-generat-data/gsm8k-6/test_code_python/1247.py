def solution():
    # Calculate the total number of cards Ellis and Orion got together
    total_cards = 500
    ellis_ratio = 11
    orion_ratio = 9
    ellis_cards = (ellis_ratio / (ellis_ratio + orion_ratio)) * total_cards
    orion_cards = (orion_ratio / (ellis_ratio + orion_ratio)) * total_cards

    # Calculate the difference between the number of cards Ellis and Orion got
    difference = ellis_cards - orion_cards
    result = difference
    return result

print(solution())