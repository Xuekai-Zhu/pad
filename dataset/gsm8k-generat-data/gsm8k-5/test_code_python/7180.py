def solution():
    sodas_per_guest = 2  # Fred is assuming each guest will drink 2 sodas
    num_guests = 15  # Fred is inviting 15 people to the party
    sodas_per_pack = 6  # Each pack of sodas contains 6 cans
    pack_cost = 3.00  # Each pack of sodas costs $3.00

    # Calculate the total number of sodas needed
    total_sodas = sodas_per_guest * num_guests

    # Calculate the total number of packs needed
    total_packs = total_sodas / sodas_per_pack
    if total_sodas % sodas_per_pack != 0:
        total_packs += 1

    # Calculate the total cost of the sodas
    total_cost = total_packs * pack_cost
    result = total_cost
    return result

print(solution())