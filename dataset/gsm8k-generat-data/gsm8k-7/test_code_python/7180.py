def solution():
    num_guests = 15
    num_sodas_per_guest = 2
    sodas_per_pack = 6
    cost_per_pack = 3.0

    # Calculate the total number of sodas needed for the party
    total_sodas_needed = num_guests * num_sodas_per_guest

    # Calculate the total number of soda packs needed for the party
    total_packs_needed = total_sodas_needed / sodas_per_pack

    # Calculate the total cost of all soda packs needed for the party
    total_cost = total_packs_needed * cost_per_pack
    result = total_cost
    return result

print(solution())