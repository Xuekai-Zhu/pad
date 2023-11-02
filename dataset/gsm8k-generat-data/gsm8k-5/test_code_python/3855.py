def solution():
    boxes_per_week = 30  # Meadow orders 30 boxes of diapers weekly
    packs_per_box = 40  # Each box contains 40 packs of diapers
    diapers_per_pack = 160  # Each pack has 160 diapers
    price_per_diaper = 5  # Meadow sells each diaper for $5

    # Calculate the total number of diapers Meadow is ordering weekly
    total_diapers = boxes_per_week * packs_per_box * diapers_per_pack

    # Calculate the total revenue from selling all the diapers
    total_revenue = total_diapers * price_per_diaper
    result = total_revenue
    return result

print(solution())