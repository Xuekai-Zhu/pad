def solution():
    excel_percent = 0.2  # 20% of candidates have experience with Excel
    day_shift_percent = 0.7  # 70% of candidates are only willing to work day shifts
    # To find the percentage of candidates who know Excel and are willing to work nights, we need to subtract the percentage of candidates who know Excel and only want to work day shifts from the total percentage of candidates who are willing to work nights
    excel_and_night_shift_percent = (1 - day_shift_percent) * excel_percent  

    result = excel_and_night_shift_percent
    return result

print(solution())