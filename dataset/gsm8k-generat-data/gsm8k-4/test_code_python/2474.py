def solution():
    """Nissa is calculating a jail sentence for a man who was convicted of burglary. The base sentence is 1 year of jail for every $5,000 of goods stolen. The burglar is going to have his sentence length increased by 25% because this is his third offense, plus 2 additional years for resisting arrest. How many years total is the burglar's sentence if he stole $40,000 worth of goods?"""
    # Define the base sentence length per $5,000 of goods stolen
    base_sentence_length = 1

    # Determine the number of $5,000 units in the value of goods stolen
    stolen_units = 40000 / 5000

    # Calculate the base sentence length for the burglary
    base_sentence = stolen_units * base_sentence_length

    # Calculate the additional sentence length for the burglary (25% increase for third offense plus 2 years for resisting arrest)
    additional_sentence = (base_sentence * 0.25) + 2

    # Calculate the total sentence length for the burglary
    total_sentence = base_sentence + additional_sentence

    result = total_sentence
    return result

print(solution())