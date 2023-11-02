def solution():
    # Calculate the total length of the ropes
    total_length = 8 + 20 + 3 * 2 + 7  # sum of all the rope lengths

    # Calculate the length lost due to knots
    knots_lost = 4 * 1.2  # 4 knots between the ropes, and each knot makes him lose 1.2 foot

    # Calculate the final length of the rope
    final_length = total_length - knots_lost
    result = final_length
    return result

print(solution())