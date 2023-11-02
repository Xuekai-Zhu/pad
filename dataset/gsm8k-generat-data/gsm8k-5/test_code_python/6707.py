def solution():
    starting_sheep = 400  # Mary has 400 sheep on her farm
    quarter_sheep = starting_sheep / 4  # Mary gives a quarter of her sheep to her sister
    remaining_sheep = starting_sheep - quarter_sheep  # Calculate the remaining sheep
    half_sheep = remaining_sheep / 2  # Mary gives half of the remaining sheep to her brother
    sheep_left = remaining_sheep - half_sheep  # Calculate how many sheep are left with Mary
    result = sheep_left
    return result

print(solution())