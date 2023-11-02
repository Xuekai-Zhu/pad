def solution():
    """To let Ruth know how long her fish will live, her father tells her that well-cared fish can live 2 years longer than dogs live. On average, dogs live 4 times as long as hamsters live. And hamsters live an average of 2.5 years. How long can a fish live?"""
    # Define the lifespan of a hamster
    hamster_lifespan = 2.5

    # Calculate the lifespan of a dog
    dog_lifespan = hamster_lifespan * 4

    # Calculate the lifespan of a well-cared fish
    fish_lifespan = dog_lifespan + 2

    # Return the result
    result = fish_lifespan
    return result

print(solution())