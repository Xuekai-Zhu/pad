def solution():
    num_horses = 100
    num_sheep = 29
    num_chickens = 9

    # Calculate the total number of animals in the barn
    total_animals = num_horses + num_sheep + num_chickens

    # Calculate the number of animals Brian bought and sold at the market
    animals_sold = total_animals / 2

    # Subtract the animals sold from the total number of animals to get the number of animals remaining in the barn
    animals_remaining = total_animals - animals_sold

    # Calculate the number of male animals in the barn
    num_male_animals = animals_remaining / 2

    # Add in the 37 goats gifted by Jeremy
    total_animals = animals_remaining + 37

    # Calculate the new number of male animals in the barn
    new_num_male_animals = total_animals / 2

    result = new_num_male_animals
    return result

print(solution())