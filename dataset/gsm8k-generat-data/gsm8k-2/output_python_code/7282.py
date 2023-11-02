def solution():
    """A farmer plants his vegetables in neat rows. He has 64 bean seedlings and plants 8 seedlings in a row. He also has 84 pumpkin seeds and plants 7 seeds in a row. Recently, he planted 48 radishes with 6 radishes in a row. If the farmer plants two rows per plant bed, how many plant beds did he have for all his plants?"""
    bean_seedlings = 64
    pumpkin_seeds = 84
    radishes = 48
    bean_rows = bean_seedlings / 8
    pumpkin_rows = pumpkin_seeds / 7
    radish_rows = radishes / 6
    total_rows = bean_rows + pumpkin_rows + radish_rows
    plant_beds = total_rows / 2
    result = plant_beds
    return result

print(solution())