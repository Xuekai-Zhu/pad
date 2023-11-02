def solution():
    """Cindy has 37 envelopes. If Cindy gives 3 envelopes to each of her 5 friends, how many envelopes does she have left?"""
    # Define the initial number of envelopes and the number of friends
    initial_envelopes = 37
    num_friends = 5

    # Calculate the number of envelopes given to friends
    envelopes_given = num_friends * 3

    # Calculate the number of envelopes remaining
    envelopes_remaining = initial_envelopes - envelopes_given

    # return the result
    result = envelopes_remaining
    return result

print(solution())