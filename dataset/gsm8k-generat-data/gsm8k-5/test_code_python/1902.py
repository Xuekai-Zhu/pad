def solution():
    antelopes = 80
    rabbits = antelopes + 34
    total_antelopes_and_rabbits = antelopes + rabbits
    hyenas = total_antelopes_and_rabbits - 42
    wild_dogs = hyenas + 50
    leopards = rabbits / 2

    # Calculate the total number of animals counted
    total_count = antelopes + rabbits + hyenas + wild_dogs + leopards
    result = total_count
    return result

print(solution())