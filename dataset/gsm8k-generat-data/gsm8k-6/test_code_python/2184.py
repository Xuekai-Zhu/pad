def solution():
    # Find the number of cats Frankie has
    cats = 6

    # Find the number of snakes Frankie has
    snakes = cats + 6

    # Find the number of parrots Frankie has
    parrots = cats - 1

    # Calculate the total number of pets Frankie has
    total_pets = cats + snakes + parrots + 6 + 2  # 6 pets with 4 legs and 2 dogs

    result = total_pets
    return result

print(solution())