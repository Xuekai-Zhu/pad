def solution():
    max_pet_beds = 12 + 8  # Lucas can fit 8 more pet beds in his room, bringing total to 20
    max_pets = max_pet_beds / 2  # Each pet needs 2 beds to feel comfortable according to Lucas' parents

    result = max_pets
    return result

print(solution())