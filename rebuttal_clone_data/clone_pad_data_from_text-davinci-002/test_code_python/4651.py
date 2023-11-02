def solution():
    aprons_needed = 150
    aprons_sewn = 13
    aprons_sewn_today = aprons_sewn * 3
    aprons_left = aprons_needed - aprons_sewn_today
    aprons_to_sew_tomorrow = aprons_left / 2
    result = aprons_to_sew_tomorrow
    return result

print(solution())