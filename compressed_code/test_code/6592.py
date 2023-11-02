def solution():
    
    susie_rhode_reds = 11
    susie_golden_comets = 6
    britney_rhode_reds = susie_rhode_reds * 2
    britney_golden_comets = susie_golden_comets / 2
    susie_total_chickens = susie_rhode_reds + susie_golden_comets
    britney_total_chickens = britney_rhode_reds + britney_golden_comets
    difference = britney_total_chickens - susie_total_chickens
    result = difference
    return result

print(solution())