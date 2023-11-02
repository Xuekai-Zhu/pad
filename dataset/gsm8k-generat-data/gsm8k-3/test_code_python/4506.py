def solution():
    """Jean is wanted on 3 counts of arson, 2 burglary charges, and six times as many petty larceny as burglary charges. If each arson count has a 36-month sentence, each burglary charge is 18 months and each petty larceny charge is 1/3rd as long as a burglary charge, how many months in jail is Jean facing?"""
    # Define the sentence length for each type of charge
    ARSON_SENTENCE = 36
    BURGLARY_SENTENCE = 18
    PETTY_LARCENY_SENTENCE = BURGLARY_SENTENCE / 3

    # Define the number of each type of charge Jean is facing
    arson_counts = 3
    burglary_counts = 2
    petty_larceny_counts = burglary_counts * 6

    # Calculate the total sentence length
    total_sentence = (arson_counts * ARSON_SENTENCE) + (burglary_counts * BURGLARY_SENTENCE) + (petty_larceny_counts * PETTY_LARCENY_SENTENCE)

    # Display the total sentence length
    result = total_sentence
    return result

print(solution())