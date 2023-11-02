def solution():
    clay_pots_on_monday = 12
    clay_pots_on_tuesday = 2 * clay_pots_on_monday
    clay_pots_on_wednesday = clay_pots_on_tuesday + clay_pots_on_monday
    total_clay_pots = 12 + 24 + clay_pots_on_wednesday
    result = total_clay_pots
    return result

print(solution())