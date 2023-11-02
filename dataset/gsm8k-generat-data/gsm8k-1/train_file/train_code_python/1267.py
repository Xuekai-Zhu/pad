def solution():
    """The toothpaste in Anne's family's bathroom contains 105 grams. Anne's dad uses 3 grams at each brushing, her mom uses 2 grams, Anne and her brother use 1 gram each. Each member of the family brushes their teeth three times a day. How many days will it take for the toothpaste to run out?"""
    total_toothpaste = 105
    grams_per_day = (3+2+1+1) * 3
    days_until_empty = total_toothpaste // grams_per_day
    result = days_until_empty
    return result

print(solution())