def solution():
    """In Fred the Farmer's barn, there were 100 horses, 29 sheep, and 9 chickens. Brian bought half of the animals and sold them at the market. Jeremy then gifted Fred an additional 37 goats. If exactly half of the animals in the barn are male animals, how many male animals are there in the barn?"""
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