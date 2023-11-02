def solution():
    """Miles is a musician. He owns three fewer trumpets than he has fingers, and two more guitars than he has hands. He also owns two more trombones than he has heads, and one fewer French horn than he has guitars. What is the total number of musical instruments that Miles owns?"""
    # Define the number of fingers, hands, and heads Miles has
    fingers = 10
    hands = 2
    heads = 1

    # Calculate the number of trumpets Miles has
    trumpets = fingers - 3

    # Calculate the number of guitars Miles has
    guitars = hands + 2

    # Calculate the number of trombones Miles has
    trombones = heads + 2

    # Calculate the number of French horns Miles has
    french_horns = guitars - 1

    # Calculate the total number of musical instruments Miles owns
    total_instruments = trumpets + guitars + trombones + french_horns

    result = total_instruments
    return result

print(solution())