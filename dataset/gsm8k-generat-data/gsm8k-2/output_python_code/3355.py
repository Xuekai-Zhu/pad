def solution():
    """Angel has written letters to all of her pen pals and is putting all of the letters in envelopes. Most of the letters are put into large envelopes and the remaining 20 letters are put into small envelopes. The large envelopes each contain 2 letters each. If Angel has written a total of 80 letters, how many large envelopes did she use?"""
    total_letters = 80
    small_envelopes = 20
    large_envelopes = (total_letters - small_envelopes) / 2
    result = large_envelopes
    return result

print(solution())