def solution():
    num_guppies_per_betta = 7
    num_betta_fish = 5
    num_guppies_per_day_for_betta = num_guppies_per_betta * num_betta_fish

    num_guppies_per_moray_eel = 20

    # Calculate the total number of guppies needed per day
    total_guppies_per_day = num_guppies_per_moray_eel + num_guppies_per_day_for_betta
    result = total_guppies_per_day
    return result

print(solution())