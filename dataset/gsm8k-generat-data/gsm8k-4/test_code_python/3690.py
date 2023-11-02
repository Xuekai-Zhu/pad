def solution():
    """Sandy's monthly phone bill expense is equal to ten times her age now. In two years, Sandy will be three times as old as Kim. If Kim is currently 10 years old, calculate Sandy's monthly phone bill expense."""
    # Define Kim's current age
    kim_age = 10

    # Calculate Sandy's age now and in two years
    sandy_age_now = None
    sandy_age_2years = sandy_age_now + 2

    # Calculate the ratio of Sandy's age in two years to Kim's age in two years
    ratio = sandy_age_2years / (kim_age + 2)

    # Calculate Sandy's current phone bill expense
    sandy_phone_bill = sandy_age_now * 10

    # Calculate Sandy's phone bill expense in two years
    sandy_phone_bill_2years = sandy_age_2years * 10

    # Calculate the amount by which Sandy's phone bill expense will increase in two years
    increase = sandy_phone_bill_2years - sandy_phone_bill

    # Calculate Sandy's new phone bill expense based on the ratio of her age to Kim's age in two years
    sandy_new_phone_bill = (increase * ratio) + sandy_phone_bill

    result = sandy_new_phone_bill
    return result

print(solution())