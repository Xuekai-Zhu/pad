def solution():
    """Mille is making snack packs for her kindergarten class. She's going to divide 64 pretzels, four times as many goldfish, and 32 suckers into baggies for the 16 kids in the class. How many items does each baggie have?"""
    pretzels = 64
    goldfish = pretzels * 4
    suckers = 32
    num_of_baggies = 16
    total_items = pretzels + goldfish + suckers
    items_per_baggie = total_items // num_of_baggies
    result = items_per_baggie
    return result

print(solution())