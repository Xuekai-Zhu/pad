def solution():
    """Melanie is a door-to-door saleswoman. She sold a third of her vacuum cleaners at the green house, 2 more to the red house, and half of what was left at the orange house. If Melanie has 5 vacuum cleaners left, how many did she start with?"""
    final_vacuum_cleaners = 5
    orange_houses = final_vacuum_cleaners * 2
    left_vacuum_cleaners = orange_houses * 2
    red_houses = left_vacuum_cleaners - 2
    initial_vacuum_cleaners = red_houses * 3
    result = initial_vacuum_cleaners

    return result

print(solution())