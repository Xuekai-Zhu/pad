def solution():
    total_letters = 80  # Angel has written a total of 80 letters
    small_envelopes = 20  # 20 letters are put into small envelopes
    large_envelopes = (total_letters - small_envelopes) / 2  # The remaining letters are put into large envelopes, with each envelope containing 2 letters
    result = large_envelopes
    return result

print(solution())