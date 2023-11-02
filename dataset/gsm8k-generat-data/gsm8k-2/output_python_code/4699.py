def solution():
    """McKenna has 34 stuffed animals. Kenley has twice as many as McKenna. Tenly has 5 more than Kenley. How many stuffed animals do the three girls have in all?"""
    mckenna_animals = 34
    kenley_animals = 2 * mckenna_animals
    tenly_animals = kenley_animals + 5
    total_animals = mckenna_animals + kenley_animals + tenly_animals
    result = total_animals
    return result

print(solution())