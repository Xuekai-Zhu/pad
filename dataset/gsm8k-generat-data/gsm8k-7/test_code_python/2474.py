def solution():
    goods_stolen = 40000
    base_sentence = goods_stolen / 5000 # each $5000 = 1 year sentence
    increased_sentence = base_sentence * 0.25 # 25% increase for third offense
    additional_years = 2 # 2 additional years for resisting arrest

    # Calculate total sentence in years
    total_sentence = base_sentence + increased_sentence + additional_years
    result = total_sentence
    return result

print(solution())