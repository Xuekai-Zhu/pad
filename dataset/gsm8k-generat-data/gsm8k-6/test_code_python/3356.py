def solution():
    # Calculate the number of small envelopes
    small_envelopes = 20

    # Calculate the number of letters in large envelopes
    large_envelopes_letters = 2

    # Calculate the total number of letters in large envelopes
    total_large_envelopes_letters = (80 - small_envelopes)

    # Calculate the number of large envelopes used
    large_envelopes = total_large_envelopes_letters // large_envelopes_letters

    result = large_envelopes
    return result

print(solution())