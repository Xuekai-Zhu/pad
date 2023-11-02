def solution():
    arson_sentence = 6 * 2  # Each count of arson carries a 6-year sentence
    explosives_sentence = arson_sentence * 2  # The explosives sentence is twice as long as the total arson sentence
    terrorism_sentence = 20  # The domestic terrorism charge carries a 20-year sentence

    # Calculate the total sentence
    total_sentence = arson_sentence + explosives_sentence + terrorism_sentence
    result = total_sentence
    return result

print(solution())