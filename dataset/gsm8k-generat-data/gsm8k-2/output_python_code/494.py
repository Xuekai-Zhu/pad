def solution():
    """Mille is making snack packs for her kindergarten class. She's going to divide 64 pretzels, four times as many goldfish, and 32 suckers into baggies for the 16 kids in the class. How many items does each baggie have?"""
    pretzels = 64
    goldfish = 4 * pretzels
    suckers = 32
    total_items = pretzels + goldfish + suckers
    items_per_baggie = total_items / 16
    result = items_per_baggie
    return result

print(solution())