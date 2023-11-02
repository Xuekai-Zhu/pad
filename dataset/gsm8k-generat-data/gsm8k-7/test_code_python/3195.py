def solution():
    packs_of_sodas = 5
    sodas_per_pack = 12
    starting_sodas = 10
    days = 7

    # Calculate the total number of sodas James has
    total_sodas = starting_sodas + (packs_of_sodas * sodas_per_pack)

    # Calculate the daily consumption of sodas
    sodas_per_day = total_sodas / days
    result = sodas_per_day
    return result

print(solution())