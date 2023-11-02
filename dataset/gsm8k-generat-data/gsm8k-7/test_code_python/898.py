def solution():
    rope_lengths = [8, 20, 2, 2, 2, 7]
    knot_length_loss = 1.2
    total_rope_length = sum(rope_lengths)

    num_knots = len(rope_lengths) - 1
    total_knot_length_loss = num_knots * knot_length_loss

    final_rope_length = total_rope_length - total_knot_length_loss
    result = final_rope_length
    return result

print(solution())