def solution():
    stolen_goods = 40000  # dollars worth of goods stolen
    base_sentence = (stolen_goods / 5000) * 1  # base jail sentence in years
    increased_sentence = base_sentence * 1.25  # increased sentence for third offense
    total_sentence = increased_sentence + 2  # additional 2 years for resisting arrest
    result = total_sentence
    return result

print(solution())