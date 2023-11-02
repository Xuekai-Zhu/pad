def solution():
    arson_counts = 3
    burglary_charges = 2
    petty_larceny_charges = 6 * burglary_charges
    sentence_for_arson = 36
    sentence_for_burglary = 18
    sentence_for_petty_larceny = sentence_for_burglary / 3
    total_months = sentence_for_arson * arson_counts + sentence_for_burglary * burglary_charges + sentence_for_petty_larceny * petty_larceny_charges
    result = total_months
    return result

print(solution())