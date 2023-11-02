def solution():
    """Cindy has 37 envelopes. If Cindy gives 3 envelopes to each of her 5 friends, how many envelopes does she have left?"""
    # Define the number of envelopes Cindy has
    num_envelopes = 37

    # Define the number of friends Cindy has
    num_friends = 5

    # Calculate the number of envelopes Cindy gives away
    envelopes_given_away = num_friends * 3

    # Calculate the number of envelopes Cindy has left
    envelopes_left = num_envelopes - envelopes_given_away

    # Display the number of envelopes Cindy has left
    result = envelopes_left
    return result

print(solution())