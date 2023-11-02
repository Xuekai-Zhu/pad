def solution():
    """Enrico owns a rooster farm, he sells each rooster for $0.50 per kilogram. He was able to sell a 30-kilogram rooster and a 40-kilogram rooster, how much money was he able to earn?"""
    # Define the price per kilogram of rooster
    price_per_kg = 0.5

    # Define the weight of the roosters
    rooster1_weight = 30
    rooster2_weight = 40

    # Calculate the total earnings from selling the roosters
    total_earnings = (rooster1_weight + rooster2_weight) * price_per_kg

    result = total_earnings
    return result

print(solution())