def solution():
    """Josie counted 80 antelopes, 34 more rabbits than antelopes, 42 fewer hyenas than the total number of antelopes and rabbits combined, 50 more wild dogs than hyenas, and the number of leopards was half the number of rabbits. What was the total number of animals Josie counted?"""
    antelopes = 80
    rabbits = antelopes + 34
    total_antelopes_rabbits = antelopes + rabbits
    hyenas = total_antelopes_rabbits - 42
    wild_dogs = hyenas + 50
    leopards = rabbits / 2
    total_animals = antelopes + rabbits + hyenas + wild_dogs + leopards
    result = total_animals
    return result

print(solution())