def solution():
    # Calculate the total number of sodas bought by Tina
    sodas_bought = 3 * 12  # 3 packs of 12 sodas

    # Calculate the total number of sodas consumed at the party
    sodas_consumed = (6 / 2) * 3 + 2 * 4 + 5  # half of the people have 3 sodas each, 2 people have 4, and 1 person has 5

    # Calculate the number of sodas left over
    sodas_left = sodas_bought - sodas_consumed
    result = sodas_left
    return result

print(solution())