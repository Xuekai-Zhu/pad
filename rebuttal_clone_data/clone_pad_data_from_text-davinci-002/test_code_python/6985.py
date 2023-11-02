def solution():
    hours_worked = 8
    hourly_wage = 9
    racquets_strung = 7
    racquet_stringing_pay = 15
    grommets_changed = 2
    grommet_changing_pay = 10
    stencils_painted = 5
    stencil_painting_pay = 1
    
    total_pay = hours_worked * hourly_wage + racquets_strung * racquet_stringing_pay + grommets_changed * grommet_changing_pay + stencils_painted * stencil_painting_pay
    result = total_pay
    
    return result

print(solution())