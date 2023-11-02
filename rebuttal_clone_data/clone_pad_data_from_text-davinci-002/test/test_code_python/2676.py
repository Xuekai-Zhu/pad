def solution():
    dresses_sewn_1 = 2
    dresses_sewn_2 = 3
    days_sewn_1 = 7
    days_sewn_2 = 2
    total_dresses_sewn = (dresses_sewn_1 * days_sewn_1) + (dresses_sewn_2 * days_sewn_2)
    ribbons_needed = total_dresses_sewn * 2
    result = ribbons_needed
    return result

print(solution())