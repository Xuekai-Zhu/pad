def solution():
    
    hourly_rate = 9
    restrung_racquets = 7
    grommet_sets_changed = 2
    stencils_painted = 5
    restrung_racquet_pay = 15 * restrung_racquets
    grommet_pay = 10 * grommet_sets_changed
    stencil_pay = 1 * stencils_painted
    total_pay = (hourly_rate * 8) + restrung_racquet_pay + grommet_pay + stencil_pay
    result = total_pay
    return result

print(solution())