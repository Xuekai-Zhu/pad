def solution():
    rent_cost = 1200
    percent_to_raise = 30
    money_needed = rent_cost - (rent_cost * (percent_to_raise / 100))
    result = money_needed
    return result

print(solution())