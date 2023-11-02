def solution():
    
    arson_count = 3
    burglary_count = 2
    petty_larceny_count = 6 * burglary_count
    arson_sentence = 36
    burglary_sentence = 18
    petty_larceny_sentence = burglary_sentence / 3
    total_sentence = (arson_count * arson_sentence) + (burglary_count * burglary_sentence) + (petty_larceny_count * petty_larceny_sentence)
    result = total_sentence
    return result

print(solution())