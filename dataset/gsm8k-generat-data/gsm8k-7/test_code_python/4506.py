def solution():
    arson_counts = 3
    arson_sentence = 36
    
    burglary_counts = 2
    burglary_sentence = 18
    
    petty_larceny_counts = burglary_counts * 6
    petty_larceny_sentence = burglary_sentence / 3
    
    total_sentence = (arson_counts * arson_sentence) + (burglary_counts * burglary_sentence) + (petty_larceny_counts * petty_larceny_sentence)
    result = total_sentence
    return result

print(solution())