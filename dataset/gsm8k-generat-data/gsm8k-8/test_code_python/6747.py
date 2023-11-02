def solution():
    # Calculate the total distance of the daily round trip
    total_distance = 21 * 2

    # Calculate the amount of gas needed for the daily commute
    daily_gas = total_distance / 30

    # Calculate the monthly gas expense
    monthly_gas_expense = daily_gas * 5 * 4 * 2.5

    # Calculate the amount each person pays towards gas
    each_person_pays = monthly_gas_expense / 5
    result = each_person_pays
    return result

print(solution())