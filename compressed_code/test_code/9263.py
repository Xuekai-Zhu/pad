def solution():
    
    rows_of_corn = 5
    corn_per_row = 80
    corn_stalks_per_bushel = 8
    total_corn_stalks = rows_of_corn * corn_per_row
    bushels_of_corn = total_corn_stalks // corn_stalks_per_bushel
    result = bushels_of_corn
    return result

print(solution())