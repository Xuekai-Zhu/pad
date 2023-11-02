def solution():
    """In Fred the Farmer's barn, there were 100 horses, 29 sheep, and 9 chickens. Brian bought half of the animals and sold them at the market. Jeremy then gifted Fred an additional 37 goats. If exactly half of the animals in the barn are male animals, how many male animals are there in the barn?"""
    # Define the initial number of animals in the barn
    horses = 100
    sheep = 29
    chickens = 9

    # Calculate the total number of initial animals
    total_animals = horses + sheep + chickens

    # Calculate the number of animals purchased by Brian
    purchased_animals = total_animals / 2

    # Calculate the number of animals left after Brian sold his animals
    remaining_animals = total_animals - purchased_animals

    # Calculate the number of animals needed to reach half males
    male_animals_needed = remaining_animals / 2

    # Calculate the number of goats gifted by Jeremy
    goats = 37

    # Calculate the number of male animals in the barn
    male_animals = male_animals_needed - goats

    result = male_animals
    return result

print(solution())