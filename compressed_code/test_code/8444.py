def solution():
    
    total_letters = 80
    small_envelopes = 20
    letters_in_large_envelopes = 2
    letters_in_small_envelopes = 1
    letters_in_large_envelopes_only = total_letters - small_envelopes
    large_envelopes_used = letters_in_large_envelopes_only / letters_in_large_envelopes
    result = large_envelopes_used
    return result

print(solution())