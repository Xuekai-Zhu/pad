def solution():
    """Two-thirds of all the animals on my street are cats and the rest are dogs.  If there are 300 animals on the street, what's the total number of legs of dogs that are on the street?"""
    # Define the total number of animals and the ratio of cats to dogs
    total_animals = 300
    cat_ratio = 2/3

    # Calculate the number of cats and dogs
    cats = total_animals * cat_ratio
    dogs = total_animals - cats

    # Calculate the total number of legs of the dogs
    dog_legs = dogs * 4

    # Return the result
    result = dog_legs
    return result

print(solution())