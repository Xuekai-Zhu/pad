def solution():
    """Frankie's parents let him have many pets. He has six more snakes than he has cats. He has one less parrot than cats. Six of his pets have four legs. He has 2 dogs. How many pets does he have in total?"""
    dogs = 2
    four_legged = 6
    cats = four_legged - dogs
    snakes = cats + 6
    parrots = cats - 1
    total_pets = dogs + four_legged + cats + snakes + parrots
    result = total_pets
    return result

print(solution())