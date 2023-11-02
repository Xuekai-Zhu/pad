def solution():
    fingers = 10  # Miles has 10 fingers
    hands = 2  # Miles has 2 hands
    heads = 1  # Miles has 1 head

    # Calculate the number of trumpets Miles owns
    trumpets = fingers - 3

    # Calculate the number of guitars Miles owns
    guitars = (hands * 2) + 2

    # Calculate the number of trombones Miles owns
    trombones = heads + 2

    # Calculate the number of French horns Miles owns
    french_horns = guitars - 1

    # Calculate the total number of musical instruments Miles owns
    total_instruments = trumpets + guitars + trombones + french_horns
    result = total_instruments
    return result

print(solution())