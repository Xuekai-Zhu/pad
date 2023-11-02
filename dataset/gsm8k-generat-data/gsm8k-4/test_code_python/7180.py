def solution():
    """Fred was having a party and was responsible for buying canned soda. He figured every guest would drink 2 sodas and he was inviting 15 people to the party. The local store had a deal on sodas that week. Every 6 pack of canned sodas was on sale for $3.00. How much would it cost Fred to buy enough sodas for every guest to have 2 cans?"""
    # Define the number of guests and cans per guest
    guests = 15
    cans_per_guest = 2

    # Calculate the total number of cans needed
    total_cans = guests * cans_per_guest

    # Calculate the number of six-packs needed
    six_packs = total_cans / 6

    # Round up to the nearest whole number of six-packs needed, and calculate the total cost
    total_cost = math.ceil(six_packs) * 3.0

    result = total_cost
    return result

print(solution())