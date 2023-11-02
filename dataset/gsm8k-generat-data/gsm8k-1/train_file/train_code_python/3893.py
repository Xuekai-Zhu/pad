def solution():
    """Tony drives a car that gets 25 miles to the gallon. He drives 50 miles round trip to work 5 days a week. His tank holds 10 gallons. He begins the week with a full tank and when he runs out he fills up at the local gas station for $2 a gallon. How much money does Tony spend on gas in 4 weeks?"""
    miles_per_week = 50 * 5
    gallons_per_week = miles_per_week / 25
    fill_ups_per_week = gallons_per_week / 10
    total_fill_ups = fill_ups_per_week * 4
    total_gallons = total_fill_ups * 10
    total_cost = total_gallons * 2
    result = total_cost
    return result

print(solution())