def solution():
    
    # Define the number of animals that need to be bathed, cats, and wings trimmed
    bathed_animals = 8
    cats_animals = 5
    wings_trimmed_animals = 3
    horses_animals = 12

    # Calculate the total number of animals that need to be groomed
    total_animals = bathed_animals + cats_animals + wings_trimmed_animals + horses_animals

    # Calculate the number of days Melissa will split the grooming jobs evenly
    days = 7

    # Calculate the number of animals that Melissa will groom each day
    animals_per_day = total_animals / days

    # Display the number of animals that Melissa will groom each day
    result = animals_per_day
    return result

print(solution())