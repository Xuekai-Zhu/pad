def solution():
    """Cindy has 37 envelopes. If Cindy gives 3 envelopes to each of her 5 friends, how many envelopes does she have left?"""
    num_envelopes = 37
    num_friends = 5
    envelopes_given = num_friends * 3
    envelopes_left = num_envelopes - envelopes_given
    result = envelopes_left
    return result

print(solution())