def solution():
    """In Fred the Farmer's barn, there were 100 horses, 29 sheep, and 9 chickens. Brian bought half of the animals and sold them at the market. Jeremy then gifted Fred an additional 37 goats. If exactly half of the animals in the barn are male animals, how many male animals are there in the barn?"""
    # Define the number of each type of animal in the barn
    horses = 100
    sheep = 29
    chickens = 9

    # Calculate the total number of animals
    total_animals = horses + sheep + chickens

    # Calculate the number of animals bought and sold by Brian
    bought_sold = total_animals / 2

    # Calculate the current number of animals in the barn
    current_animals = total_animals - bought_sold + 37

    # Calculate the number of male animals in the barn
    male_animals = current_animals / 2

    # Display the number of male animals
    result = male_animals
    return result

print(solution())