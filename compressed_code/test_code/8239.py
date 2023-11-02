def solution():
    
    graphics_card_cost = 600
    hard_drive_cost = 80
    cpu_cost = 200
    ram_pair_cost = 60

    graphics_card_total = 10 * graphics_card_cost
    hard_drive_total = 14 * hard_drive_cost
    cpu_total = 8 * cpu_cost
    ram_pair_total = 4 * ram_pair_cost

    total_earnings = graphics_card_total + hard_drive_total + cpu_total + ram_pair_total
    result = total_earnings
    return result

print(solution())