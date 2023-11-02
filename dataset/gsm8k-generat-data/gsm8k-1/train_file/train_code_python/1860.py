def solution():
    """Two-thirds of all the animals on my street are cats and the rest are dogs. If there are 300 animals on the street, what's the total number of legs of dogs that are on the street?"""
    total_animals = 300
    cat_ratio = 2/3
    dog_ratio = 1 - cat_ratio
    
    # Assuming all cats and dogs have 4 legs
    total_legs = total_animals * 4
    
    # Number of legs of dogs on the street
    dog_legs = total_legs * dog_ratio
    result = dog_legs
    return result

print(solution())