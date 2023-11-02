def solution():
    """Angel has written letters to all of her pen pals and is putting all of the letters in envelopes. Most of the letters are put into large envelopes and the remaining 20 letters are put into small envelopes. The large envelopes each contain 2 letters each. If Angel has written a total of 80 letters, how many large envelopes did she use?"""
    # Calculate the number of small envelopes used
    small_envelopes = 20

    # Calculate the number of letters in the large envelopes
    large_envelope_letters = 2

    # Calculate the total number of letters in the large envelopes
    large_envelope_total = 80 - small_envelopes

    # Calculate the number of large envelopes used
    large_envelopes = large_envelope_total // large_envelope_letters

    result = large_envelopes
    return result

print(solution())