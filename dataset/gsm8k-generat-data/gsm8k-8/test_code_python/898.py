def solution():
    # Define the length of each rope
    rope_lengths = [8, 20, 2, 2, 2, 7]

    # Define the total length of the rope
    total_length = sum(rope_lengths)

    # Define the number of knots
    num_knots = len(rope_lengths) - 1

    # Subtract the length lost from the knots
    length_lost = num_knots * 1.2

    # Calculate the final length
    final_length = total_length - length_lost
    result = final_length
    return result

print(solution())