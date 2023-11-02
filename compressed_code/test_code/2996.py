def solution():
    
    boxes_per_week = 30
    packs_per_box = 40
    diapers_per_pack = 160
    diapers_per_week = boxes_per_week * packs_per_box * diapers_per_pack
    price_per_diaper = 5
    total_earnings = diapers_per_week * price_per_diaper
    result = total_earnings
    return result

print(solution())