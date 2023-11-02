def solution():
    """Sandy's monthly phone bill expense is equal to ten times her age now. In two years, Sandy will be three times as old as Kim. If Kim is currently 10 years old, calculate Sandy's monthly phone bill expense."""
    # Define Kim's age and the number of years from now when Sandy will be three times as old as Kim
    KIM_AGE = 10
    YEARS_FROM_NOW = 2

    # Calculate Sandy's current age
    sandy_current_age = (KIM_AGE * 3) - YEARS_FROM_NOW

    # Calculate Sandy's monthly phone bill expense
    phone_bill_expense = 10 * sandy_current_age

    # Display Sandy's monthly phone bill expense
    result = phone_bill_expense
    return result

print(solution())