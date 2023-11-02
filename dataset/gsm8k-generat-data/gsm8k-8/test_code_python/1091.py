def solution():
    # Calculate the number of bottles Harper drinks in 1 day
    daily_bottles = 0.5

    # Calculate the total bottles needed for 240 days
    total_bottles = daily_bottles * 240

    # Calculate the number of cases needed, rounding up to the nearest whole number
    cases_needed = math.ceil(total_bottles / 24)

    # Calculate the total cost of the cases
    case_cost = 12.0
    total_cost = cases_needed * case_cost

    result = total_cost
    return result

print(solution())