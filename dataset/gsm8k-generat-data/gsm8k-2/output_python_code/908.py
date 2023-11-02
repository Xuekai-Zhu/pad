def solution():
    """In a compound, the number of cats is 20% less than the number of dogs. There are also twice as many frogs as the number of dogs in the compound. Calculate the total number of animals present in the compound if there are 160 frogs."""
    frog_count = 160
    dog_count = frog_count / 2
    cat_count = 0.8 * dog_count
    total_animals = frog_count + dog_count + cat_count
    result = total_animals
    return result

print(solution())