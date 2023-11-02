def solution():
    antelopes = 80
    rabbits = antelopes + 34
    hyenas = antelopes + rabbits - 42
    wild_dogs = hyenas + 50
    leopards = rabbits / 2
    total = antelopes + rabbits + hyenas + wild_dogs + leopards
    result = total
    return result

print(solution())