def solution():
    """Fred was having a party and was responsible for buying canned soda. He figured every guest would drink 2 sodas and he was inviting 15 people to the party. The local store had a deal on sodas that week. Every 6 pack of canned sodas was on sale for $3.00. How much would it cost Fred to buy enough sodas for every guest to have 2 cans?"""
    sodas_per_guest = 2
    total_guests = 15
    sodas_needed = sodas_per_guest * total_guests
    sodas_per_pack = 6
    packs_needed = sodas_needed / sodas_per_pack
    pack_price = 3
    total_price = packs_needed * pack_price
    result = total_price
    return result

print(solution())