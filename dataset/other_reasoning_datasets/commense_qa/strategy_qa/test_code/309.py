def solution():
    golden_age_start_year = 1650
    golden_age_end_year = 1720
    ark_length = 450
    queen_annes_revenge_length = 103
    adventure_galley_length = 124
    if ark_length > queen_annes_revenge_length and ark_length > adventure_galley_length and golden_age_start_year < 450 < golden_age_end_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())