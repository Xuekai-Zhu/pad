def solution():
    num_pieces = 10
    piece_length = 6
    long_rope_length = 6 * 12  # convert 6 feet to inches
    long_rope_cost = 5.0
    short_rope_length = 1 * 12  # convert 1 foot to inches
    short_rope_cost = 1.25

    # Calculate the total length of rope needed
    total_length = num_pieces * piece_length

    # Calculate the number of long ropes needed
    num_long_ropes = total_length // long_rope_length

    # Calculate the length of short rope needed
    remaining_length = total_length - (num_long_ropes * long_rope_length)
    num_short_ropes = remaining_length // short_rope_length

    # Calculate the total cost
    cost = (num_long_ropes * long_rope_cost) + (num_short_ropes * short_rope_cost)
    result = cost
    return result

print(solution())