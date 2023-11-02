def solution():
    yuri_squares = 2 + 4 + 5  # Total squares Yuri moved
    yuko_dice = [1, 5]  # Yuko's first two dice rolls
    possible_moves = []  # List to store all possible moves for Yuko's last die

    # Loop through all possible values for Yuko's last die
    for i in range(1, 7):
        yuko_squares = yuko_dice[0] + yuko_dice[1] + i  # Total squares Yuko would move

        # Check if Yuko's total squares moved would be greater than Yuri's
        if yuko_squares > yuri_squares:
            # Append the number of squares moved by Yuko's last die to the list of possible moves
            possible_moves.append(yuko_squares - yuri_squares)

    # Return the minimum number of squares Yuko must move to be in front of his brother
    result = min(possible_moves)
    return result

print(solution())