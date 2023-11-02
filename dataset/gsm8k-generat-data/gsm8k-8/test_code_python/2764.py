def solution():
    # Calculate the total number of animals in the barn
    total_animals = 100 + 29 + 9

    # Calculate the number of animals Brian bought and sold
    bought_sold = total_animals / 2

    # Calculate the number of goats that Jeremy gifted to Fred
    goats = 37

    # Calculate the current number of animals in the barn
    current_animals = total_animals - bought_sold + goats

    # Calculate the number of male animals in the barn
    male_animals = current_animals / 2

    result = male_animals
    return result

print(solution())