def solution():
    # Calculate the total sentence before extension
    total_sentence = 3 + 24  # 3 months for assault and 2 years (24 months) for poisoning

    # Calculate the extended sentence
    extended_sentence = total_sentence + (total_sentence/3)

    # Convert extended sentence to months
    months_in_jail = extended_sentence * 12

    result = months_in_jail
    return result

print(solution())