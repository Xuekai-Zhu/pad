def solution():
    """Cherry put up a delivery service. She charges $2.50 for a 3-5 kilograms cargo and $4 for a 6-8 kilograms cargo.
    If she delivers four 5 kilograms cargo and two 8 kilograms cargo per day, how much money will she earn in a week?"""
    kg5_cost = 2.5
    kg8_cost = 4
    kg5_cargo = 4
    kg8_cargo = 2
    weekly_earnings = (kg5_cost * kg5_cargo * 7) + (kg8_cost * kg8_cargo * 7)
    result = weekly_earnings
    return result

print(solution())