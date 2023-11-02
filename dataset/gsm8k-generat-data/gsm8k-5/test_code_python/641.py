def solution():
    silk_per_dress = 5  # Each dress needs 5 meters of silk
    total_silk = 600  # Alex has 600 meters of silk in storage
    num_friends = 5  # Alex gives silk to 5 friends
    silk_given_to_friends = 20 * num_friends  # Each friend gets 20 meters of silk
    silk_remaining = total_silk - silk_given_to_friends  # Alex uses the rest to make dresses

    # Calculate the number of dresses Alex can make
    num_dresses = silk_remaining // silk_per_dress
    result = num_dresses
    return result

print(solution())