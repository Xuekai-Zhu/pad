def solution():
     people_attending = 15
     sodas_per_person = 2
     sodas_needed = people_attending * sodas_per_person
     packs_needed = sodas_needed / 6
     price_per_pack = 3
     total_price = packs_needed * price_per_pack
 
     result = total_price
     return result

print(solution())