def solution():
    """Artemis is making tea for a party. She knows her mom drinks an 8-ounce cup of tea and uses one ounce of tea. She will use this same ratio for the party. The party has 12 people there and each of them wants a 6-ounce cup of tea. How many ounces of tea does she need?"""
    # Define the ratio of tea to cup size
    tea_ratio = 1 / 8

    # Define the number of cups needed for the party
    cups_needed = 12

    # Define the size of each cup
    cup_size = 6

    # Calculate the total amount of tea needed
    total_tea = cups_needed * cup_size * tea_ratio

    result = total_tea
    return result

print(solution())