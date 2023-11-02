def solution():
    """Remi wants to drink more water. He has a refillable water bottle that holds 20 ounces of water. That week Remi refills the bottle 3 times a day and drinks the whole bottle each time except for twice when he accidentally spills 5 ounces the first time and 8 ounces the second time. In 7 days how many ounces of water does Remi drink?"""
    water_bottle_size = 20
    refills_per_day = 3
    days = 7
    ounces_per_refill = water_bottle_size - 5 - 8
    total_refills = refills_per_day * days
    total_ounces = ounces_per_refill * total_refills
    result = total_ounces
    return result

print(solution())