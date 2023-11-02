def solution():
    """Artemis is making tea for a party. She knows her mom drinks an 8-ounce cup of tea and uses one ounce of tea. She will use this same ratio for the party. The party has 12 people there and each of them wants a 6-ounce cup of tea. How many ounces of tea does she need?"""
    ounces_per_cup = 8
    ounces_of_tea = 1
    cups_of_tea = 12
    ounces_needed = cups_of_tea * (ounces_per_cup / ounces_of_tea)
    result = ounces_needed
    return result

print(solution())