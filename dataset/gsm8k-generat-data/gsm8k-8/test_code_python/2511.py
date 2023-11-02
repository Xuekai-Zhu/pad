def solution():
    # Define the length of sentence for each charge
    arson_sentence = 6
    explosives_sentence = 2 * arson_sentence
    terrorism_sentence = 20

    # Calculate the total length of sentence
    total_sentence = 2 * arson_sentence + explosives_sentence + terrorism_sentence

    result = total_sentence
    return result

print(solution())