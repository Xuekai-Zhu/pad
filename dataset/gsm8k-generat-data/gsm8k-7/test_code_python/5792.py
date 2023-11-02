def solution():
    num_envelopes = 37
    num_friends = 5
    envelopes_per_friend = 3

    # Calculate the total number of envelopes given to friends
    total_envelopes_given_to_friends = num_friends * envelopes_per_friend

    # Calculate the number of envelopes Cindy has left
    envelopes_left = num_envelopes - total_envelopes_given_to_friends
    result = envelopes_left
    return result

print(solution())