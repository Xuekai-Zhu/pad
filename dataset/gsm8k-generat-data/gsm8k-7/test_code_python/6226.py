def solution():
    num_3_egg_omelettes_1st_hour = 5
    num_4_egg_omelettes_2nd_hour = 7
    num_3_egg_omelettes_3rd_hour = 3
    num_4_egg_omelettes_4th_hour = 8

    num_eggs_3_egg_omelette = 3
    num_eggs_4_egg_omelette = 4

    # Calculate the total number of 3 egg omelettes
    total_3_egg_omelettes = num_3_egg_omelettes_1st_hour + num_3_egg_omelettes_3rd_hour

    # Calculate the total number of 4 egg omelettes
    total_4_egg_omelettes = num_4_egg_omelettes_2nd_hour + num_4_egg_omelettes_4th_hour

    # Calculate the total number of eggs needed
    total_num_eggs = (total_3_egg_omelettes * num_eggs_3_egg_omelette) + (total_4_egg_omelettes * num_eggs_4_egg_omelette)
    result = total_num_eggs
    return result

print(solution())