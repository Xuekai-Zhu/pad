def solution():
    """Tanesha needs to buy rope so cut into 10 pieces that are each six inches long. She sees a 6-foot length of rope that cost $5 and also sees 1-foot lengths of rope that cost $1.25 each. What is the least she has to spend to get the rope she needs?"""
    # Define the length and cost of the 6-foot rope
    rope_length = 6  # in feet
    rope_cost = 5

    # Define the length and cost of the 1-foot rope
    segment_length = 1  # in feet
    segment_cost = 1.25

    # Calculate the total rope length needed in inches
    total_length = 10 * 6  # in inches

    # Calculate the number of segments needed
    num_segments = total_length / (segment_length * 12)

    # Round up to the nearest integer
    num_segments = int(num_segments) + 1  # add 1 extra segment for safety

    # Calculate the total cost of buying the necessary segments
    total_cost = num_segments * segment_cost

    # Choose the least cost option
    if total_cost < rope_cost:
        least_cost = total_cost
    else:
        least_cost = rope_cost

    result = least_cost
    return result

print(solution())