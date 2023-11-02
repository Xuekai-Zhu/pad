def solution():
    num_litters = 3
    num_babies_per_litter = 8
    fraction_given_away = 1/6
    fraction_sold_to_pet_store = 3/6
    fraction_sold_to_snake_owners = 1/2

    # Calculate the total number of babies
    total_babies = num_litters * num_babies_per_litter

    # Calculate the number given away
    num_given_away = total_babies * fraction_given_away

    # Calculate the number sold to pet store
    num_sold_to_pet_store = total_babies * fraction_sold_to_pet_store

    # Calculate the number remaining
    num_remaining = total_babies - num_given_away - num_sold_to_pet_store

    # Calculate the number sold to snake owners
    num_sold_to_snake_owners = num_remaining * fraction_sold_to_snake_owners

    # Calculate the number of remaining mice
    num_remaining = num_remaining - num_sold_to_snake_owners

    result = num_remaining
    return result

print(solution())