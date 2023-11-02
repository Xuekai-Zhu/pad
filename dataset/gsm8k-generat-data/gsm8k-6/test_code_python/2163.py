def solution():
    fingers = 10
    hands = 2
    heads = 1

    trumpets = fingers - 3
    guitars = hands + 2
    trombones = heads + 2
    french_horns = guitars - 1

    total_instruments = trumpets + guitars + trombones + french_horns

    result = total_instruments
    return result

print(solution())