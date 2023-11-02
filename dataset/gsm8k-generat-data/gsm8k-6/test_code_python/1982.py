def solution():
    # Calculate the total length of the walls
    total_length = 2*4 + 2*6  # 2 walls are 4 meters wide and 2 walls are 6 meters wide

    # Multiply the total length by 2 to cover both sides of the walls
    total_tape_length = total_length * 2

    result = total_tape_length
    return result

print(solution())