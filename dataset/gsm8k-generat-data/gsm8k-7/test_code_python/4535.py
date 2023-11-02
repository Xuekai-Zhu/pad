def solution():
    num_chickens = 26
    num_piglets = 40
    num_goats = 34

    # Calculate the total number of animals before the storm
    total_animals = num_chickens + num_piglets + num_goats

    # Calculate the number of animals that get sick
    num_sick_animals = total_animals / 2
    result = num_sick_animals
    return result

print(solution())