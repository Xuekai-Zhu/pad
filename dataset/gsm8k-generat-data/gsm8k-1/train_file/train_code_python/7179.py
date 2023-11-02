def solution():
    """Fred was having a party and was responsible for buying canned soda. He figured every guest would drink 2 sodas and he was inviting 15 people to the party. The local store had a deal on sodas that week. Every 6 pack of canned sodas was on sale for $3.00. How much would it cost Fred to buy enough sodas for every guest to have 2 cans?"""
    guests = 15
    sodas_per_guest = 2
    sodas_per_pack = 6
    price_per_pack = 3
    packs_needed = (guests * sodas_per_guest) / sodas_per_pack
    cost = packs_needed * price_per_pack
    result = cost
    return result

print(solution())