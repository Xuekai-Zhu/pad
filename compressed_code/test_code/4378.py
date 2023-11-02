def solution():
    
    num_of_packs = 2
    sheets_per_pack = 240
    total_sheets = num_of_packs * sheets_per_pack
    sheets_per_day = 80
    days_of_use = total_sheets // sheets_per_day
    result = days_of_use
    return result

print(solution())