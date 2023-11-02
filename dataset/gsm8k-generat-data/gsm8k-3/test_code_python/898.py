def solution():
    """Tony wants to build the longest rope he possibly can, so he collects all the rope in his home. He finds an 8-foot rope, a 20-foot rope, three 2 foot ropes, and a 7-foot rope. each knot between the ropes makes him lose 1.2 foot per knot. How long is his rope when he's done tying them all together?"""
    # Define the length of each rope
    rope_lengths = [8, 20, 2, 2, 2, 7]

    # Calculate the total length of the ropes before tying and knotting
    total_length = sum(rope_lengths)

    # Calculate the total length lost due to knots
    knot_length = (len(rope_lengths) - 1) * 1.2

    # Calculate the final length after tying and knotting
    final_length = total_length - knot_length

    # Display the final length of the rope
    result = final_length
    return result

print(solution())