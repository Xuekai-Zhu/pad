def solution():
    """Meadow has a business that sells baby diapers to her local townspeople. She orders 30 boxes of diapers containing 40 packs weekly, with each pack having 160 diapers. She sells each diaper for $5. How much money is Meadow making from selling all her diapers?"""
    boxes_per_week = 30
    packs_per_box = 40
    diapers_per_pack = 160
    price_per_diaper = 5
    total_diapers = boxes_per_week * packs_per_box * diapers_per_pack
    total_sales = total_diapers * price_per_diaper
    result = total_sales
    return result

print(solution())