def solution():
    """Cindy has 37 envelopes. If Cindy gives 3 envelopes to each of her 5 friends, how many envelopes does she have left?"""
    starting_envelopes = 37
    envelopes_given_per_friend = 3
    num_friends = 5
    envelopes_given_away = envelopes_given_per_friend * num_friends
    envelopes_left = starting_envelopes - envelopes_given_away
    result = envelopes_left
    return result

print(solution())