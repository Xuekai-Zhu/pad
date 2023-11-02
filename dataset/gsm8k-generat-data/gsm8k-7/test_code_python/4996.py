def solution():
    num_packs = 3
    num_sodas_in_pack = 6
    num_sodas_drunk_per_day = 0.5
    num_weeks = 4

    # Calculate the total number of sodas Rebecca bought
    total_num_sodas_bought = num_packs * num_sodas_in_pack

    # Calculate the total number of sodas Rebecca will drink in four weeks
    total_num_sodas_drunk = num_weeks * 7 * num_sodas_drunk_per_day

    # Calculate the number of sodas Rebecca will have left after four weeks
    num_sodas_left = total_num_sodas_bought - total_num_sodas_drunk
    result = num_sodas_left
    return result

print(solution())