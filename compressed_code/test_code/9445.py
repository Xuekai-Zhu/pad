def solution():
    
    total_aprons = 150
    aprons_sewn = 13
    today_aprons = 3 * aprons_sewn
    remaining_aprons = total_aprons - aprons_sewn - today_aprons
    aprons_to_sew_tomorrow = remaining_aprons / 2
    result = aprons_to_sew_tomorrow
    return result

print(solution())