def solution():
    """Legoland has 5 kangaroos for each koala. If Legoland has 180 kangaroos, how many koalas and kangaroos are there altogether?"""
    kangaroos = 180
    koalas = kangaroos / 5
    total_animals = kangaroos + koalas
    result = total_animals
    return result

print(solution())