def solution():
    # Define the number of counts for each charge type
    arson_counts = 3
    burglary_counts = 2
    petty_larceny_counts = 6 * burglary_counts

    # Define the sentence length for each charge type
    arson_sentence = 36
    burglary_sentence = 18
    petty_larceny_sentence = burglary_sentence / 3

    # Calculate the total sentence length for each charge type
    total_arson_sentence = arson_counts * arson_sentence
    total_burglary_sentence = burglary_counts * burglary_sentence
    total_petty_larceny_sentence = petty_larceny_counts * petty_larceny_sentence

    # Calculate the total sentence length for all charges
    total_sentence = total_arson_sentence + total_burglary_sentence + total_petty_larceny_sentence
    result = total_sentence
    return result

print(solution())