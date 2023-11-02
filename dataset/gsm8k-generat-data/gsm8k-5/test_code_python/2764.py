def solution():
    # Calculate the total number of animals in the barn
    total_animals = 100 + 29 + 9  # 100 horses, 29 sheep, and 9 chickens

    # Calculate the number of animals Brian bought and sold
    sold_animals = total_animals / 2

    # Calculate the number of animals remaining in the barn after Brian sold his share
    remaining_animals = total_animals - sold_animals

    # Calculate the number of male animals in the barn
    male_animals = remaining_animals / 2

    # Add the gift of 37 goats from Jeremy
    male_animals += 37 / 2

    result = male_animals
    return result

print(solution())