def solution():
    """Mille is making snack packs for her kindergarten class. She's going to divide 64 pretzels, four times as many goldfish, and 32 suckers into baggies for the 16 kids in the class. How many items does each baggie have?"""
    # Define the number of pretzels, goldfish, and suckers
    pretzels = 64
    goldfish = pretzels * 4
    suckers = 32

    # Define the number of kids in the class
    kids = 16

    # Calculate the total number of items
    total_items = pretzels + goldfish + suckers

    # Calculate the number of items in each baggie
    items_per_baggie = total_items // kids

    # return the result
    result = items_per_baggie
    return result

print(solution())