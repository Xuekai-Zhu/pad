def solution():
    num_packs = 3
    sodas_per_pack = 12
    num_people = 6

    # Calculate the total number of sodas
    total_sodas = num_packs * sodas_per_pack

    # Calculate the number of sodas consumed by half of the people
    sodas_consumed = (num_people / 2) * 3 + 2 * 4 + 5

    # Calculate the number of sodas remaining
    sodas_remaining = total_sodas - sodas_consumed
    result = sodas_remaining
    return result

print(solution())