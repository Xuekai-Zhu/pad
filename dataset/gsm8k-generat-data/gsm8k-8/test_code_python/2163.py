def solution():
    # Define the variables for the number of fingers, hands, and heads
    fingers = 10
    hands = 2
    heads = 1

    # Calculate the number of trumpets
    trumpets = fingers - 3

    # Calculate the number of guitars
    guitars = hands + 2

    # Calculate the number of trombones
    trombones = heads + 2

    # Calculate the number of French horns
    french_horns = guitars - 1

    # Calculate the total number of musical instruments
    total_instruments = trumpets + guitars + trombones + french_horns
    result = total_instruments
    return result

print(solution())