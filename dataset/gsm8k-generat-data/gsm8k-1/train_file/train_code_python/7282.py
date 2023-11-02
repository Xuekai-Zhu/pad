def solution():
    """A farmer plants his vegetables in neat rows. He has 64 bean seedlings and plants 8 seedlings in a row. He also has 84 pumpkin seeds and plants 7 seeds in a row. Recently, he planted 48 radishes with 6 radishes in a row. If the farmer plants two rows per plant bed, how many plant beds did he have for all his plants?"""
    bean_seedlings = 64
    pumpkin_seeds = 84
    radishes = 48
    beans_per_row = 8
    pumpkins_per_row = 7
    radishes_per_row = 6
    total_rows = (bean_seedlings // beans_per_row) + (pumpkin_seeds // pumpkins_per_row) + (radishes // radishes_per_row)
    plant_beds = total_rows // 2
    result = plant_beds
    return result

print(solution())