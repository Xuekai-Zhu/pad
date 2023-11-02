def solution():
    large_animal_price = 4
    num_large_animals = 2
    total_earned = 120

    # Calculate the total number of small stuffed animals sold today
    total_small_animals = (total_earned / (large_animal_price * num_large_animals)) / small_animal_price

    # Calculate the total number of small stuffed animals sold
    total_small_animals = total_small_animals / (large_animal_price * num_small_animals)
    result = total_small_animals
    return result

print(solution())