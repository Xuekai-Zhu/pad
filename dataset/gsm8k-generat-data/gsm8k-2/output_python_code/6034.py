def solution():
    """Cherry put up a delivery service. She charges $2.50 for a 3-5 kilograms cargo and $4 for a 6-8 kilograms cargo. If she delivers four 5 kilograms cargo and two 8 kilograms cargo per day, how much money will she earn in a week?"""
    price_3_5 = 2.5
    price_6_8 = 4
    cargo_weights = [5, 5, 5, 5, 8, 8]
    total_earnings = 0
    for weight in cargo_weights:
        if weight <= 5:
            total_earnings += price_3_5
        elif weight <= 8:
            total_earnings += price_6_8
    weekly_earnings = total_earnings * 7
    result = weekly_earnings
    return result

print(solution())