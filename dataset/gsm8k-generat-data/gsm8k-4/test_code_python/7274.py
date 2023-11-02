def solution():
    """20% of the job candidates at a temp agency have experience with Excel. 70% of the candidates are only willing to work day shifts. If a manager picks a candidate at random, what are the odds they know Excel and are willing to work nights?"""
    # Define the percentage of candidates with Excel experience and the percentage willing to work day shifts
    excel_percentage = 0.2
    day_shift_percentage = 0.7

    # Calculate the percentage of candidates who do not want to work day shifts
    night_shift_percentage = 1 - day_shift_percentage

    # Calculate the percentage of candidates with Excel experience who are willing to work nights
    excel_night_percentage = excel_percentage * night_shift_percentage

    # Return the result
    result = excel_night_percentage
    return result

print(solution())