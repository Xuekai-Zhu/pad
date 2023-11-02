def solution():
    total_inches = 81
    eight_inch_subs = 2
    five_inch_subs = (total_inches - (eight_inch_subs * 8)) / 5
    result = five_inch_subs
    return result

print(solution())