def solution():
    price_per_kilo = 0.5
    rooster1_weight = 30
    rooster2_weight = 40

    # Calculate the total weight of the roosters
    total_weight = rooster1_weight + rooster2_weight

    # Calculate the total earnings from selling the roosters
    total_earnings = total_weight * price_per_kilo
    result = total_earnings
    return result

print(solution())