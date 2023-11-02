def solution():
    # Calculate the total number of months in jail for Jean
    arson_sentence = 3 * 36  # 3 counts of arson with a 36-month sentence
    burglary_sentence = 2 * 18  # 2 burglary charges with an 18-month sentence each
    larceny_sentence = 6 * (1/3 * 18)  # 6 times as many petty larceny as burglary charges, with 1/3 the sentence of a burglary charge
    total_sentence = arson_sentence + burglary_sentence + larceny_sentence
    result = total_sentence
    return result

print(solution())