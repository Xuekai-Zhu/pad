def solution():
    """Angel has written letters to all of her pen pals and is putting all of the letters in envelopes. Most of the letters are put into large envelopes and the remaining 20 letters are put into small envelopes. The large envelopes each contain 2 letters each. If Angel has written a total of 80 letters, how many large envelopes did she use?"""
    total_letters = 80
    small_envelopes = 20
    letters_in_large_envelopes = 2
    letters_in_small_envelopes = 1
    letters_in_large_envelopes_only = total_letters - small_envelopes
    large_envelopes_used = letters_in_large_envelopes_only / letters_in_large_envelopes
    result = large_envelopes_used
    return result

print(solution())