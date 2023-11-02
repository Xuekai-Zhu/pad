def solution():
    
    horses = 100
    sheep = 29
    chickens = 9
    total_animals = horses + sheep + chickens
    animals_sold = total_animals / 2
    animals_remaining = total_animals - animals_sold + 37
    male_animals = animals_remaining / 2
    
    result = male_animals
    return result

print(solution())