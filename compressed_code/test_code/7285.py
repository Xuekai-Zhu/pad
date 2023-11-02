def solution():
    
    trevor_spends = 80
    reed_spends = trevor_spends - 20
    quinn_spends = reed_spends / 2
    total_spends_per_year = trevor_spends + reed_spends + quinn_spends
    total_spends_in_four_years = total_spends_per_year * 4
    result = total_spends_in_four_years
    
    return result

print(solution())