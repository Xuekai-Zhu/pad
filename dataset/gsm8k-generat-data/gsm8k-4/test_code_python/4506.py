def solution():
    """Jean is wanted on 3 counts of arson, 2 burglary charges, and six times as many petty larceny as burglary charges.
    If each arson count has a 36-month sentence, each burglary charge is 18 months and each petty larceny charge is 1/3rd
    as long as a burglary charge, how many months in jail is Jean facing?"""
    
    # Define the sentence length for each type of charge
    ARSON_SENTENCE = 36
    BURGLARY_SENTENCE = 18
    PETTY_LARCENY_SENTENCE = BURGLARY_SENTENCE / 3
    
    # Define the number of charges for each type
    ARSON_CHARGES = 3
    BURGLARY_CHARGES = 2
    PETTY_LARCENY_CHARGES = BURGLARY_CHARGES * 6
    
    # Calculate the total length of the sentence
    sentence_length = (ARSON_CHARGES * ARSON_SENTENCE) + (BURGLARY_CHARGES * BURGLARY_SENTENCE) + (PETTY_LARCENY_CHARGES * PETTY_LARCENY_SENTENCE)
    
    # Return the result
    result = sentence_length
    return result

print(solution())