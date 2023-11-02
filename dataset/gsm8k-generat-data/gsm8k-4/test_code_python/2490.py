def solution():
    """A pet store has six dogs for sale. They have half as many cats, twice as many birds, and thrice as many fish for sale. How many animals are for sale in the pet store?"""
    # Define the number of dogs
    dogs = 6

    # Calculate the number of cats, birds, and fish
    cats = dogs / 2
    birds = dogs * 2
    fish = dogs * 3

    # Calculate the total number of animals
    total_animals = dogs + cats + birds + fish

    # return the result
    result = total_animals
    return result

print(solution())