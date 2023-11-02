def solution():
    """20% of the job candidates at a temp agency have experience with Excel. 70% of the candidates are only willing to work day shifts. If a manager picks a candidate at random, what are the odds they know Excel and are willing to work nights?"""
    excel_exp = 0.2
    day_shift = 0.7
    excel_and_night = excel_exp * (1 - day_shift)
    result = excel_and_night
    return result

print(solution())