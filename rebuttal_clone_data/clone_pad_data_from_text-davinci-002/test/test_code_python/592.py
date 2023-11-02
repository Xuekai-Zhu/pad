def solution():
    susie_reds = 11
    susie_golden = 6
    britney_reds = susie_reds * 2
    britney_golden = susie_golden / 2
    total_susie = susie_reds + susie_golden
    total_britney = britney_reds + britney_golden
    result = total_britney - total_susie
    return result

print(solution())