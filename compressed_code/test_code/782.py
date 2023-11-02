def solution():
    
    susie_rhodes = 11
    susie_golden = 6
    britney_rhodes = 2 * susie_rhodes
    britney_golden = susie_golden / 2
    susie_total = susie_rhodes + susie_golden
    britney_total = britney_rhodes + britney_golden
    difference = britney_total - susie_total
    result = difference
    return result

print(solution())