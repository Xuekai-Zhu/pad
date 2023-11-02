def solution():
    total_letters = 80
    small_envelopes = 20

    # Calculate the number of letters put in large envelopes
    large_envelopes_letters = total_letters - small_envelopes

    # Calculate the number of large envelopes
    num_large_envelopes = large_envelopes_letters / 2
    result = num_large_envelopes
    return result

print(solution())