def solution():
    num_dogs = 8
    num_cats = 5
    num_wings = 3
    num_horses = 12

    # Calculate the total number of animals that need to be bathed
    total_bathed_animals = num_dogs + num_cats

    # Calculate the total number of animals that need to be trimmed
    total_wings_trimmed_animals = num_wings * num_horses

    # Calculate the total number of animals that need to be brushed
    total_groomed_animals = total_bathed_animals + total_wings_trimmed_animals + total_horses

    # Calculate the number of animals that need to be groomed each day
    animals_per_day = total_groomed_animals / 7
    result = animals_per_day
    return result

print(solution())