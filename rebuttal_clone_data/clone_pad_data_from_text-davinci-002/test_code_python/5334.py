def solution():
     pencils_used_per_week = 10
     pencils_in_pack = 30
     cost_per_pack = 4
     weeks_in_forty_five_days = 45 / 5
     pencils_needed = weeks_in_forty_five_days * pencils_used_per_week
     packs_of_pencils_needed = pencils_needed / pencils_in_pack
     cost = packs_of_pencils_needed * cost_per_pack
     result = cost
     return result

print(solution())