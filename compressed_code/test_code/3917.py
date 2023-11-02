def solution():
    
    pages_per_day = 2 * 5  
    classes_per_day = 5
    sheets_per_pack = 100
    weeks = 6
    total_pages = pages_per_day * classes_per_day * weeks
    total_packs = total_pages / sheets_per_pack
    result = total_packs
    return result

print(solution())