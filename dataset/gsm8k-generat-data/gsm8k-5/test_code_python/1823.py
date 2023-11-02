def solution():
    assault_sentence = 3  # Gerald is sentenced to 3 months for assault
    poisoning_sentence = 24  # Gerald is sentenced to 2 years (24 months) for poisoning
    total_sentence = assault_sentence + poisoning_sentence
    extended_sentence = total_sentence + (total_sentence / 3)  # Gerald's sentence is extended by a third

    result = extended_sentence
    return result

print(solution())