def solution():
    
    dresses_first_week = 2 * 7
    dresses_second_week = 3 * 2
    total_dresses = dresses_first_week + dresses_second_week
    ribbons_per_dress = 2
    total_ribbons = total_dresses * ribbons_per_dress
    result = total_ribbons
    return result

print(solution())