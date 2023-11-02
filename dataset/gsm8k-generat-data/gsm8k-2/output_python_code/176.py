def solution():
    """A store sells 20 packets of 100 grams of sugar every week. How many kilograms of sugar does it sell every week?"""
    sugar_per_packet = 100  # in grams
    packets_per_week = 20
    total_sugar = sugar_per_packet * packets_per_week / 1000  # convert to kilograms
    result = total_sugar
    return result

print(solution())