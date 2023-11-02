def solution():
    """Two-thirds of all the animals on my street are cats and the rest are dogs.  If there are 300 animals on the street, what's the total number of legs of dogs that are on the street?"""
    # Find the total number of cats and dogs on the street
    total_animals = 300
    cats = total_animals * 2 / 3
    dogs = total_animals - cats

    # Calculate the total number of dog legs
    dog_legs = dogs * 4

    # Display the total number of dog legs on the street
    result = dog_legs
    return result

print(solution())