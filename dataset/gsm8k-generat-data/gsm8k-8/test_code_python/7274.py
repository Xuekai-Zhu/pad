def solution():
    excel_experience = 0.2
    day_shift_only = 0.7

    # Calculate the odds of a candidate having Excel experience and being willing to work nights
    excel_and_night_shift = (1 - day_shift_only) * excel_experience

    result = excel_and_night_shift
    return result

print(solution())