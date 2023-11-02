def solution():
    excel_exp = 0.2
    day_shift_only = 0.7

    # Calculate the percentage of candidates who are willing to work nights
    night_shift_only = 1 - day_shift_only

    # Calculate the percentage of candidates who know Excel and are willing to work nights
    excel_and_night_shift = excel_exp * night_shift_only

    result = excel_and_night_shift
    return result

print(solution())