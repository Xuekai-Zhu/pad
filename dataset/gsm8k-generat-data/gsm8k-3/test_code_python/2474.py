def solution():
    """Nissa is calculating a jail sentence for a man who was convicted of burglary. The base sentence is 1 year of jail for every $5,000 of goods stolen. The burglar is going to have his sentence length increased by 25% because this is his third offense, plus 2 additional years for resisting arrest. How many years total is the burglar's sentence if he stole $40,000 worth of goods?"""
    # Define the base sentence per $5,000 worth of stolen goods
    BASE_SENTENCE = 1

    # Define the sentence increase multiplier for third-time offenders
    THIRD_OFFENSE_MULTIPLIER = 1.25

    # Define the additional years for resisting arrest
    RESISTING_ARREST_YEARS = 2

    # Calculate the base sentence for the amount of goods stolen
    stolen_goods = 40000
    base_sentence_years = stolen_goods // 5000 * BASE_SENTENCE

    # Calculate the sentence increase for third-time offenders
    if base_sentence_years > 0:
        sentence_increase = base_sentence_years * THIRD_OFFENSE_MULTIPLIER - base_sentence_years
    else:
        sentence_increase = 0

    # Calculate the total sentence length
    total_sentence_years = base_sentence_years + sentence_increase + RESISTING_ARREST_YEARS

    # Display the total sentence length
    result = total_sentence_years
    return result

print(solution())