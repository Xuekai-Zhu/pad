def solution():
    """The toothpaste in Anne's family's bathroom contains 105 grams. Anne's dad uses 3 grams at each brushing, her mom uses 2 grams, Anne and her brother use 1 gram each. Each member of the family brushes their teeth three times a day. How many days will it take for the toothpaste to run out?"""
    toothpaste_size = 105
    total_daily_usage = 3+2+1+1
    total_daily_usage_grams = total_daily_usage * 3
    days_until_empty = toothpaste_size // total_daily_usage_grams
    result = days_until_empty
    return result

print(solution())