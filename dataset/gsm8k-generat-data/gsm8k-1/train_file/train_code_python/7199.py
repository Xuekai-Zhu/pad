def solution():
    """Owen bred 21 turtles, and Johanna has 5 fewer turtles than Owen. After 1 month, Owen has twice as many turtles as before and Johanna loses half of her turtles and donates the rest to Owen. How many turtles did Owen have?"""
    owen_turtles = 21
    johanna_turtles = owen_turtles - 5
    owen_turtles *= 2
    johanna_turtles /= 2
    owen_turtles += johanna_turtles
    result = owen_turtles
    return result

print(solution())