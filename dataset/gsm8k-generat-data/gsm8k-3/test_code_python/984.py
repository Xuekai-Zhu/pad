def solution():
    """Legoland has 5 kangaroos for each koala. If Legoland has 180 kangaroos, how many koalas and kangaroos are there altogether?"""
    # Define the ratio of kangaroos to koalas
    KANG_KOALA_RATIO = 5

    # Define the number of kangaroos
    kangaroos = 180

    # Calculate the number of koalas
    koalas = kangaroos // KANG_KOALA_RATIO

    # Calculate the total number of animals
    total_animals = kangaroos + koalas

    # Display the total number of animals
    result = total_animals
    return result

print(solution())