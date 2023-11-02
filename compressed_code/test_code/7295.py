def solution():
    
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