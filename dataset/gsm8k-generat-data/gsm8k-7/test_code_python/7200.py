def solution():
    owen_turtles = 21
    johanna_turtles = owen_turtles - 5

    # Owen doubles his turtle count
    owen_turtles *= 2

    # Johanna loses half of her turtles
    johanna_turtles /= 2

    # Johanna donates the rest to Owen
    owen_turtles += johanna_turtles

    result = owen_turtles
    return result

print(solution())