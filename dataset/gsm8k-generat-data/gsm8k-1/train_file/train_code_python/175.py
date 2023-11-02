def solution():
    """A store sells 20 packets of 100 grams of sugar every week. How many kilograms of sugar does it sell every week?"""
    packets_per_week = 20
    grams_per_packet = 100
    total_grams = packets_per_week * grams_per_packet
    total_kilos = total_grams / 1000
    result = total_kilos
    return result

print(solution())