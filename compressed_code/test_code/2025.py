def solution():
    
    lisa_centers = 6
    jude_centers = lisa_centers / 2
    han_centers = 2 * jude_centers - 2
    jane_centers = 2 * han_centers + 6
    total_centers = lisa_centers + jude_centers + han_centers + jane_centers
    result = total_centers
    return result

print(solution())