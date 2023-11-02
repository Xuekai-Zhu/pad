def solution():
    """Mille is making snack packs for her kindergarten class. She's going to divide 64 pretzels, four times as many goldfish, and 32 suckers into baggies for the 16 kids in the class. How many items does each baggie have?"""
    # Define the number of items for each type of snack
    PRETZELS = 64
    GOLDFISH = PRETZELS * 4
    SUCKERS = 32

    # Define the number of kids in the class
    KIDS = 16

    # Calculate the number of items in each baggie for each type of snack
    pretzels_per_baggie = PRETZELS // KIDS
    goldfish_per_baggie = GOLDFISH // KIDS
    suckers_per_baggie = SUCKERS // KIDS

    # Display the number of items in each baggie
    result = (pretzels_per_baggie, goldfish_per_baggie, suckers_per_baggie)
    return result

print(solution())