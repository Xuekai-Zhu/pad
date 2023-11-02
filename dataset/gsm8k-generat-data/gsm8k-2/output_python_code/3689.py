def solution():
    """Sandy's monthly phone bill expense is equal to ten times her age now. In two years, Sandy will be three times as old as Kim. If Kim is currently 10 years old, calculate Sandy's monthly phone bill expense."""
    kim_age = 10
    sandy_future_age = 3 * (kim_age + 2)
    sandy_current_age = sandy_future_age - 2
    monthly_expense = 10 * sandy_current_age
    result = monthly_expense
    return result

print(solution())