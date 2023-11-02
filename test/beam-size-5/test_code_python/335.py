def solution():
    total_animals = 60  # Farmer Brown has 60 animals on his farm
    cows = total_animals / 3  # Farmer Brown has twice as many chickens as cows
    chickens = 2 * cows  # Farmer Brown has twice as many chickens as cows
    legs_per_animal = 4  # Each animal has 4 legs

    # Calculate the total number of legs for all animals
    total_legs = (cows * legs_per_animal) + (chickens * legs_per_animal)
    result = total_legs
    return result

print(solution())