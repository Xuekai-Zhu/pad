def solution():
    
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