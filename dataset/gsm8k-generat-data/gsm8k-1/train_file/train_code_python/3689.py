def solution():
    """Sandy's monthly phone bill expense is equal to ten times her age now. In two years, Sandy will be three times as old as Kim. If Kim is currently 10 years old, calculate Sandy's monthly phone bill expense."""
    kim_age = 10
    sandy_age_in_two_years = 3 * kim_age
    sandy_age_now = sandy_age_in_two_years - 2
    phone_bill_expense = 10 * sandy_age_now
    result = phone_bill_expense
    return result

print(solution())