def solution():
    """The toothpaste in Anne's family's bathroom contains 105 grams. Anne's dad uses 3 grams at each brushing, her mom uses 2 grams, Anne and her brother use 1 gram each. Each member of the family brushes their teeth three times a day. How many days will it take for the toothpaste to run out?"""
    # Define the amount of toothpaste in grams and the amount used per brushing for each family member
    TOOTHPASTE_AMOUNT = 105
    DAD_BRUSH_AMOUNT = 3
    MOM_BRUSH_AMOUNT = 2
    ANNE_BRUSH_AMOUNT = 1
    BROTHER_BRUSH_AMOUNT = 1

    # Calculate the total amount of toothpaste used per day by the family
    daily_total = (DAD_BRUSH_AMOUNT + MOM_BRUSH_AMOUNT + ANNE_BRUSH_AMOUNT + BROTHER_BRUSH_AMOUNT) * 3

    # Calculate the number of days the toothpaste will last
    days_last = TOOTHPASTE_AMOUNT / daily_total

    # Display the number of days the toothpaste will last
    result = days_last
    return result

print(solution())