def solution():
    """Angel has written letters to all of her pen pals and is putting all of the letters in envelopes. Most of the letters are put into large envelopes and the remaining 20 letters are put into small envelopes. The large envelopes each contain 2 letters each. If Angel has written a total of 80 letters, how many large envelopes did she use?"""
    # Calculate the number of small envelopes
    small_envelopes = 20

    # Calculate the number of letters in large envelopes
    large_envelope_letters = 2

    # Calculate the total number of letters in large envelopes
    large_envelopes = (80 - small_envelopes) / large_envelope_letters

    # Display the number of large envelopes
    result = large_envelopes
    return result

print(solution())