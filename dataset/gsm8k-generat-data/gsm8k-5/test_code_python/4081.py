def solution():
    black_shirts_per_pack = 5  # Each pack of black shirts contains 5 shirts
    yellow_shirts_per_pack = 2  # Each pack of yellow shirts contains 2 shirts
    packs_of_black_shirts = 3  # Mandy bought 3 packs of black shirts
    packs_of_yellow_shirts = 3  # Mandy bought 3 packs of yellow shirts

    # Calculate the total number of black shirts
    total_black_shirts = black_shirts_per_pack * packs_of_black_shirts

    # Calculate the total number of yellow shirts
    total_yellow_shirts = yellow_shirts_per_pack * packs_of_yellow_shirts

    # Calculate the total number of shirts Mandy bought
    total_shirts = total_black_shirts + total_yellow_shirts
    result = total_shirts
    return result

print(solution())