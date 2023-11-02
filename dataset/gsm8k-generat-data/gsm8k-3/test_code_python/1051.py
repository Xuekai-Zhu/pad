def solution():
    """The Reptile House at the zoo has 5 fewer animals than 3 times the number of animals housed in the Rain Forest exhibit. If the Reptile House has 16 animals, how many are in the Rain Forest exhibit?"""
    # Let's define the number of animals in the Rain Forest exhibit as x
    x = (16 + 5) / 3

    # We need to round up to the next integer, since we can't have a fraction of an animal
    x = int(round(x))

    # Display the answer
    result = x
    return result

print(solution())