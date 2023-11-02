def solution():
    """Together Felipe and Emilio needed a combined time of 7.5 years to build their homes. Felipe finished in half the time of Emilio. How many months did it take Felipe to build his house?"""
    total_time_years = 7.5
    felipe_time_years = total_time_years / 3
    felipe_time_months = felipe_time_years * 12
    result = felipe_time_months
    return result

print(solution())