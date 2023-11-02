def solution():
    # Calculate the total number of animals in the barn
    total_animals = 100 + 29 + 9

    # Calculate the number of animals Brian bought
    bought_animals = total_animals / 2

    # Calculate the number of animals left in the barn after Brian bought and sold his animals
    remaining_animals = total_animals - bought_animals

    # Calculate the number of male animals in the barn
    male_animals = remaining_animals / 2

    # Calculate the total number of animals after Jeremy gifted Fred the goats
    total_animals += 37

    # Calculate the remaining number of animals after Jeremy's gift
    remaining_animals += 37

    # Calculate the number of male animals after Jeremy's gift
    male_animals = remaining_animals / 2

    result = male_animals
    return result

print(solution())