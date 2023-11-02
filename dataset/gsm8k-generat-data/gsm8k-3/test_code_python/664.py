def solution():
    """To let Ruth know how long her fish will live, her father tells her that well-cared fish can live 2 years longer than dogs live. On average, dogs live 4 times as long as hamsters live. And hamsters live an average of 2.5 years. How long can a fish live?"""
    # Define the lifespan of a hamster
    HAMSTER_LIFESPAN = 2.5

    # Calculate the lifespan of a dog
    DOG_LIFESPAN = 4 * HAMSTER_LIFESPAN

    # Calculate the lifespan of a well-cared fish
    FISH_LIFESPAN = DOG_LIFESPAN + 2

    # Display the lifespan of a well-cared fish
    result = FISH_LIFESPAN
    return result

print(solution())