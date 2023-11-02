def solution():
    """Remi wants to drink more water. He has a refillable water bottle that holds 20 ounces of water. That week Remi refills the bottle 3 times a day and drinks the whole bottle each time except for twice when he accidentally spills 5 ounces the first time and 8 ounces the second time. In 7 days how many ounces of water does Remi drink?"""
    bottle_size = 20
    bottles_per_day = 3
    total_bottles = bottles_per_day * 7
    total_ounces = total_bottles * bottle_size
    total_ounces -= 5 + 8
    result = total_ounces
    return result

print(solution())