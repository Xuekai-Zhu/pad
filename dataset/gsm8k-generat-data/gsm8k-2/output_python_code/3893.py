def solution():
    """Tony drives a car that gets 25 miles to the gallon. He drives 50 miles round trip to work 5 days a week. His tank holds 10 gallons. He begins the week with a full tank and when he runs out he fills up at the local gas station for $2 a gallon. How much money does Tony spend on gas in 4 weeks?"""
    mpg = 25
    miles_per_week = 50 * 5
    gallons_per_week = miles_per_week / mpg
    tank_size = 10
    total_weeks = 4
    total_gallons = gallons_per_week * total_weeks
    cost_per_gallon = 2
    total_cost = total_gallons * cost_per_gallon
    result = total_cost
    return result

print(solution())