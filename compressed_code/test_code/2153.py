def solution():
    
    horses = 100
    sheep = 29
    chickens = 9
    total_animals = horses + sheep + chickens
    animals_sold = total_animals / 2
    remaining_animals = total_animals - animals_sold + 37
    half_animals = remaining_animals / 2
    male_animals = half_animals

    result = male_animals
    return result

print(solution())