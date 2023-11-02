def solution():
    """The toothpaste in Anne's family's bathroom contains 105 grams. Anne's dad uses 3 grams at each brushing, her mom uses 2 grams, Anne and her brother use 1 gram each. Each member of the family brushes their teeth three times a day. How many days will it take for the toothpaste to run out?"""
    # Define the initial amount of toothpaste and the amount used per day
    INITIAL_AMOUNT = 105
    AMOUNT_USED_PER_DAY = 3 * (3 + 2 + 1 + 1)

    # Calculate the number of days it will take for the toothpaste to run out
    days = INITIAL_AMOUNT / AMOUNT_USED_PER_DAY

    # Round the result to the nearest integer and return it
    result = round(days)
    return result

print(solution())