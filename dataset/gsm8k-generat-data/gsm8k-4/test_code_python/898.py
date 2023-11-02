def solution():
    """Tony wants to build the longest rope he possibly can, so he collects all the rope in his home. He finds an 8-foot rope, a 20-foot rope, three 2 foot ropes, and a 7-foot rope. each knot between the ropes makes him lose 1.2 foot per knot. How long is his rope when he's done tying them all together?"""
    # Define the initial length of the rope
    rope_length = 0

    # Add the length of each rope
    rope_length += 8
    rope_length += 20
    rope_length += 3 * 2
    rope_length += 7

    # Calculate the total length lost due to knots
    total_knot_loss = (4 - 1) * 1.2

    # Subtract the length lost due to knots
    rope_length -= total_knot_loss

    result = rope_length
    return result

print(solution())