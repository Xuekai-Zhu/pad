def solution():
    total_envelopes = 37  # Cindy has 37 envelopes
    friends = 5  # Cindy wants to give 3 envelopes to each of her 5 friends

    # Total number of envelopes that Cindy gives to her friends
    envelopes_given = 3 * friends

    # Calculate the number of envelopes that Cindy has left
    envelopes_left = total_envelopes - envelopes_given
    result = envelopes_left
    return result

print(solution())