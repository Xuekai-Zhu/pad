def solution():
    packets_per_week = 20
    grams_per_packet = 100
    grams_per_kg = 1000

    # Calculate total grams of sugar sold per week
    total_grams = packets_per_week * grams_per_packet

    # Convert grams to kilograms
    total_kg = total_grams / grams_per_kg
    result = total_kg
    return result

print(solution())