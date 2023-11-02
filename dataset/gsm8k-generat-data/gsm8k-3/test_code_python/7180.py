def solution():
    """Fred was having a party and was responsible for buying canned soda.  He figured every guest would drink 2 sodas and he was inviting 15 people to the party.  The local store had a deal on sodas that week.  Every 6 pack of canned sodas was on sale for $3.00.  How much would it cost Fred to buy enough sodas for every guest to have 2 cans?"""
    # Define the number of sodas needed for each guest
    SODAS_PER_GUEST = 2

    # Define the number of guests
    num_guests = 15

    # Calculate the total number of sodas needed
    total_sodas_needed = SODAS_PER_GUEST * num_guests

    # Calculate the number of 6-packs needed
    num_6_packs_needed = total_sodas_needed / 6
    num_6_packs_needed = round(num_6_packs_needed)
    if num_6_packs_needed < 1:
        num_6_packs_needed = 1

    # Calculate the total cost of the sodas
    cost_per_6_pack = 3.00
    total_cost = num_6_packs_needed * cost_per_6_pack

    # Display the total cost
    result = total_cost
    return result

print(solution())