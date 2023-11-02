def solution():
    """Two-thirds of all the animals on my street are cats and the rest are dogs. If there are 300 animals on the street, what's the total number of legs of dogs that are on the street?"""
    total_animals = 300
    cats = total_animals * (2/3)  # two-thirds are cats
    dogs = total_animals - cats  # rest are dogs
    dog_legs = dogs * 4  # assuming all dogs have 4 legs
    result = dog_legs
    return result

print(solution())