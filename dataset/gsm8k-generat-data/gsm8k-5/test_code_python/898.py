def solution():
    ropes = [8, 20, 2, 2, 2, 7]  # Tony has ropes of lengths 8, 20, 2, 2, 2, and 7 feet
    knots = len(ropes) - 1  # Number of knots between the ropes

    # Calculate the total length of the ropes
    total_length = sum(ropes)

    # Calculate the length lost due to the knots
    length_lost = knots * 1.2

    # Calculate the final length of the rope
    final_length = total_length - length_lost
    result = final_length
    return result

print(solution())