def solution():
    packs = 3  # Tina buys 3 packs of soda
    drinks_per_pack = 12  # Each pack contains 12 sodas
    total_drinks = packs * drinks_per_pack  # Total sodas

    people_at_party = 6  # 6 people are at the party
    total_guests = people_at_party - 1  # Total guests (excluding Tina)

    half_guests = total_guests // 2
    remaining_guests = total_guests - half_guests

    # Calculate the total number of sodas consumed
    sodas_consumed = (half_guests * 3) + (2 * 4) + 5

    # Calculate the number of sodas left over
    sodas_left = total_drinks - sodas_consumed
    result = sodas_left
    return result

print(solution())