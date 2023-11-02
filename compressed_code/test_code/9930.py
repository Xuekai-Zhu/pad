def solution():
    
    total_apples = 34
    ripe_apples = total_apples - 6
    apples_per_pie = 4
    pies_can_make = ripe_apples // apples_per_pie
    result = pies_can_make
    return result

print(solution())