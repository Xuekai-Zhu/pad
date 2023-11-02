def solution():
    
    graphics_cards_sold = 10
    hard_drives_sold = 14
    cpus_sold = 8
    ram_pairs_sold = 4
    graphics_card_price = 600
    hard_drive_price = 80
    cpu_price = 200
    ram_pair_price = 60
    graphics_cards_total_price = graphics_cards_sold * graphics_card_price
    hard_drives_total_price = hard_drives_sold * hard_drive_price
    cpus_total_price = cpus_sold * cpu_price
    ram_pairs_total_price = ram_pairs_sold * ram_pair_price
    total_earnings = graphics_cards_total_price + hard_drives_total_price + cpus_total_price + ram_pairs_total_price
    result = total_earnings
    return result

print(solution())