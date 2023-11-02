def solution():
    """Miles is a musician. He owns three fewer trumpets than he has fingers, and two more guitars than he has hands. He also owns two more trombones than he has heads, and one fewer French horn than he has guitars. What is the total number of musical instruments that Miles owns?"""
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