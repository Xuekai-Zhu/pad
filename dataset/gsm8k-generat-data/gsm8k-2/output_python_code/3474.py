def solution():
    """Kim has 12 nail polishes. Heidi has 5 more nail polishes than Kim, and Karen has 4 fewer nail polishes than Kim. How many nail polishes does Karen and Heidi have together?"""
    kim_polishes = 12
    heidi_polishes = kim_polishes + 5
    karen_polishes = kim_polishes - 4
    total_polishes = heidi_polishes + karen_polishes
    result = total_polishes
    return result

print(solution())