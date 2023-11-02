def solution():
     boxes_ordered = 30
     packs_per_box = 40
     diapers_per_pack = 160
     price_per_diaper = 5
     total_diapers = boxes_ordered * packs_per_box * diapers_per_pack
     total_revenue = total_diapers * price_per_diaper
     result = total_revenue
     return result

print(solution())