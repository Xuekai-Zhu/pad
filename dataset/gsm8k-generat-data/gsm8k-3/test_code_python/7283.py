def solution():
    """A farmer plants his vegetables in neat rows. He has 64 bean seedlings and plants 8 seedlings in a row. He also has 84 pumpkin seeds and plants 7 seeds in a row. Recently, he planted 48 radishes with 6 radishes in a row. If the farmer plants two rows per plant bed, how many plant beds did he have for all his plants?"""
    # Calculate the number of bean rows and pumpkin rows
    bean_rows = 64 // 8
    pumpkin_rows = 84 // 7

    # Calculate the number of radish rows
    radish_rows = 48 // 6

    # Calculate the total number of plant rows
    total_rows = bean_rows + pumpkin_rows + radish_rows

    # Calculate the number of plant beds needed
    plant_beds = total_rows // 2

    # Display the number of plant beds needed
    result = plant_beds
    return result

print(solution())