def solution():
    
    donuts_bought = 2.5 * 12
    donuts_left_after_driving = donuts_bought * 0.9
    donuts_left_after_afternoon_snack = donuts_left_after_driving - 4
    result = donuts_left_after_afternoon_snack
    return result

print(solution())