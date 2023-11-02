def solution():
    total_cows_sheep = 4 + 3  # Dany has 4 cows and 3 sheep
    total_chickens = 7  # Dany has 7 chickens
    total_bushels_per_day = (total_cows_sheep + total_chickens) * 2 + total_chickens * 3  # Total bushels required per day

    result = total_bushels_per_day
    return result

print(solution())