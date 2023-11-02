def solution():
    """Josie and her family went on a safari and had an exciting time watching different animals grazing and playing together. She decided to count each animal she saw and calculated their total number. She counted 80 antelopes, 34 more rabbits than antelopes, 42 fewer hyenas than the total number of antelopes and rabbits combined, 50 more wild dogs than hyenas, and the number of leopards was half the number of rabbits. What the total number of animals that Josie counted?"""
    antelopes = 80
    rabbits = antelopes + 34
    hyenas = (antelopes + rabbits) - 42
    wild_dogs = hyenas + 50
    leopards = rabbits / 2
    total_animals = antelopes + rabbits + hyenas + wild_dogs + leopards
    result = total_animals
    return result

print(solution())