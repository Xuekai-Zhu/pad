def solution():
    # Kim's current age
    kim_age = 10

    # In two years, Kim will be:
    kim_future_age = kim_age + 2

    # Sandy's age in two years, when she will be three times as old as Kim
    sandy_future_age = 3 * kim_future_age

    # Sandy's current age
    sandy_age = sandy_future_age - 2

    # Sandy's monthly phone bill expense
    monthly_bill = 10 * sandy_age
    result = monthly_bill
    return result

print(solution())