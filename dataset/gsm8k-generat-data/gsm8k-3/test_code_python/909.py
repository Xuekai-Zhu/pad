def solution():
    """In a compound, the number of cats is 20% less than the number of dogs. There are also twice as many frogs as the number of dogs in the compound. Calculate the total number of animals present in the compound if there are 160 frogs."""
    # Define the number of frogs and the ratio of cats to dogs
    frogs = 160
    cat_to_dog_ratio = 0.8

    # Calculate the number of dogs and cats in the compound
    dogs = frogs / 2
    cats = cat_to_dog_ratio * dogs

    # Calculate the total number of animals in the compound
    total_animals = dogs + cats + frogs

    # Display the total number of animals
    result = total_animals
    return result

print(solution())