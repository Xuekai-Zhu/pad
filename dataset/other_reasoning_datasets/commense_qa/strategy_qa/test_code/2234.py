def solution():
    bloomberg_worth = 60_000_000_000
    micronesia_expenses_per_year = 200_000_000
    years_to_fund = 10
    total_cost = micronesia_expenses_per_year * years_to_fund
    if bloomberg_worth > total_cost:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())