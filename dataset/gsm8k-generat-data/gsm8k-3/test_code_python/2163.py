def solution():
    """Miles is a musician.  He owns three fewer trumpets than he has fingers, and two more guitars than he has hands.  He also owns two more trombones than he has heads, and one fewer French horn than he has guitars.  What is the total number of musical instruments that Miles owns?"""
    # Define the number of fingers and hands Miles has
    fingers = 10
    hands = 2

    # Calculate the number of trumpets and guitars Miles owns
    trumpets = fingers - 3
    guitars = hands + 2

    # Calculate the number of heads and French horns Miles owns
    heads = 1
    trombones = heads + 2
    french_horns = guitars - 1

    # Calculate the total number of musical instruments Miles owns
    total_instruments = trumpets + guitars + trombones + french_horns

    # Display the total number of musical instruments
    result = total_instruments
    return result

print(solution())