def solution():
    """Jean is wanted on 3 counts of arson, 2 burglary charges, and six times as many petty larceny as burglary charges. If each arson count has a 36-month sentence, each burglary charge is 18 months and each petty larceny charge is 1/3rd as long as a burglary charge, how many months in jail is Jean facing?"""
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