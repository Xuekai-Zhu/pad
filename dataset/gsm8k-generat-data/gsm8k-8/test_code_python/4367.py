def solution():
    # Define the starting and ending spaces
    start_space = 0
    end_space = 48

    # Calculate the spaces Susan has already moved
    spaces_moved = 8 + 2 - 5 + 6

    # Calculate the remaining spaces to win the game
    remaining_spaces = end_space - start_space - spaces_moved
    result = remaining_spaces
    return result

print(solution())