def solution():
    corn_rows = 10
    corn_cobs_per_row = 9
    potato_rows = 5
    potatoes_per_row = 30
    pest_damage = 0.5  # 50% of crops destroyed by pests

    # Calculate the total number of corn cobs produced
    total_corn_cobs = corn_rows * corn_cobs_per_row

    # Calculate the total number of potatoes produced
    total_potatoes = potato_rows * potatoes_per_row

    # Calculate the total number of crops
    total_crops = total_corn_cobs + total_potatoes

    # Calculate the number of crops remaining after pest damage
    remaining_crops = total_crops * (1 - pest_damage)

    result = remaining_crops
    return result

print(solution())