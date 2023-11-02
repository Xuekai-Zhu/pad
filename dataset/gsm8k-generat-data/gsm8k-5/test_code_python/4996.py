def solution():
    sodas_per_pack = 6  # Each pack contains 6 sodas
    total_sodas = sodas_per_pack * 3  # Rebecca bought three 6-packs of soda
    sodas_per_day = 0.5  # Rebecca drinks half a bottle of soda a day
    days_per_week = 7  # There are 7 days in a week
    weeks = 4  # Rebecca wants to know how many sodas she will have left after 4 weeks

    # Calculate the total number of sodas Rebecca will drink in 4 weeks
    total_sodas_drunk = sodas_per_day * days_per_week * weeks

    # Calculate the total number of sodas Rebecca will have left after 4 weeks
    total_sodas_left = total_sodas - total_sodas_drunk
    result = total_sodas_left
    return result

print(solution())