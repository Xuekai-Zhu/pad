def solution():
    total_spaces = 48  # Total number of spaces on the board game
    current_position = 8  # Susan starts at the 8th space
    current_turn = 3  # Susan has already completed two turns

    # Calculate the remaining number of spaces Susan needs to reach the end
    while current_position < total_spaces:
        current_turn += 1
        if current_turn % 2 == 1:  # Odd turns: move forward
            current_position += 6
        else:  # Even turns: move forward and backward
            current_position += 2
            current_position -= 5

    required_moves = current_position - total_spaces
    result = required_moves
    return result

print(solution())