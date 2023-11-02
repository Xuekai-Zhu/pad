def solution():
    goods_stolen = 40000  # Burglar stole $40,000 worth of goods
    base_sentence = goods_stolen / 5000  # Calculate base sentence in years
    sentence_increase = base_sentence * 0.25  # Calculate sentence increase for third offense
    resisting_arrest = 2  # Additional 2 years for resisting arrest

    # Calculate total sentence length
    total_sentence = base_sentence + sentence_increase + resisting_arrest
    result = total_sentence
    return result

print(solution())