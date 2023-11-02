def solution():
    """Legoland has 5 kangaroos for each koala. If Legoland has 180 kangaroos, how many koalas and kangaroos are there altogether?"""
    # Define the number of kangaroos
    kangaroos = 180

    # Calculate the number of koalas as 1/5th of the number of kangaroos
    koalas = kangaroos / 5

    # Calculate the total number of animals
    total_animals = kangaroos + koalas

    # Return the result
    result = total_animals
    return result

print(solution())