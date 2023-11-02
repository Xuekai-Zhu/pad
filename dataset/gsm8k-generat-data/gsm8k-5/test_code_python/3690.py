def solution():
    kim_age_in_2_years = 10 + 2  # Kim's age in 2 years will be her current age plus 2
    sandy_age_in_2_years = kim_age_in_2_years * 3  # Sandy's age in 2 years will be 3 times Kim's age

    # Calculate Sandy's current age
    sandy_age_now = sandy_age_in_2_years - 2

    # Calculate Sandy's monthly phone bill expense
    monthly_expense = sandy_age_now * 10
    result = monthly_expense
    return result

print(solution())