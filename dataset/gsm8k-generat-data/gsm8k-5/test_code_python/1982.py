def solution():
    # Calculate the total width of the walls
    total_width = (2 * 4) + (2 * 6)  # Two walls are 4 meters wide and two walls are 6 meters wide

    # Calculate the total length of masking tape needed to cover the width of the walls
    total_length = total_width * 2  # Elijah needs to cover both the top and bottom of each wall

    result = total_length
    return result

print(solution())