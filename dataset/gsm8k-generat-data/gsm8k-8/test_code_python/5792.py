def solution():
    # Define the initial number of envelopes
    num_envelopes = 37

    # Calculate the total number of envelopes given to friends
    envelopes_given = 3 * 5

    # Calculate the number of envelopes remaining
    envelopes_left = num_envelopes - envelopes_given
    result = envelopes_left
    return result

print(solution())