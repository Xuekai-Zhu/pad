def solution():
    marthas_rats = 3
    marthas_birds = 7

    # Calculate the total number of animals Martha's cat catches
    marthas_animals = marthas_rats + marthas_birds

    # Calculate the number of animals Cara's cat catches
    caras_animals = (5 * marthas_animals) - 3

    result = caras_animals
    return result

print(solution())