def solution():
    arson_counts = 3
    burglary_charges = 2
    petty_larceny_charges = 6 * burglary_charges
    
    arson_sentence = 36
    burglary_sentence = 18
    petty_larceny_sentence = burglary_sentence / 3
    
    total_arson_sentence = arson_counts * arson_sentence
    total_burglary_sentence = burglary_charges * burglary_sentence
    total_petty_larceny_sentence = petty_larceny_charges * petty_larceny_sentence
    
    total_sentence = total_arson_sentence + total_burglary_sentence + total_petty_larceny_sentence
    
    result = total_sentence
    return result

print(solution())