def solution():
    """A pet store has six dogs for sale. They have half as many cats, twice as many birds, and thrice as many fish for sale. How many animals are for sale in the pet store?"""
    # Define the number of dogs for sale
    dogs = 6

    # Calculate the number of cats for sale
    cats = dogs / 2

    # Calculate the number of birds for sale
    birds = dogs * 2

    # Calculate the number of fish for sale
    fish = dogs * 3

    # Calculate the total number of animals for sale
    total_animals = dogs + cats + birds + fish

    # Display the total number of animals for sale
    result = total_animals
    return result

print(solution())