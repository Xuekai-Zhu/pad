def solution():
    """Jay & Gloria were hosting a 4th of July party at their house. Jay invited 22 people and Gloria invited 36. They wanted to buy small American flags for everyone. The craft store was having a sale on small flags, 5 flags for $1.00. If they wanted all of their guests to have a flag and they also wanted 1 flag each, how much would they spend at the craft store?"""
    
    jay_guests = 22
    gloria_guests = 36
    total_guests = jay_guests + gloria_guests
    flags_per_person = 6
    flags_per_pack = 5
    pack_price = 1
    total_flags = flags_per_person * total_guests
    total_packs = total_flags // flags_per_pack + 1
    total_price = total_packs * pack_price
    result = total_price
    return result

print(solution())