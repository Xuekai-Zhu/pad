def solution():
    """Enrico owns a rooster farm, he sells each rooster for $0.50 per kilogram. He was able to sell a 30-kilogram rooster and a 40-kilogram rooster, how much money was he able to earn?"""
    price_per_kg = 0.50
    rooster1_weight = 30
    rooster2_weight = 40
    total_weight = rooster1_weight + rooster2_weight
    total_earnings = total_weight * price_per_kg
    result = total_earnings
    return result

print(solution())