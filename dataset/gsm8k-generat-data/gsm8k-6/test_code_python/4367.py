def solution():
    # Calculate the total number of spaces Susan has moved after three turns
    total_spaces = 8 + 2 - 5 + 6  # she moves forward 8 spaces on first turn, 2 spaces on second turn but lands on a space that sends her back 5 spaces, and 6 spaces on third turn
    # Calculate the number of spaces left to the winning end space of the game
    spaces_left = 48 - total_spaces
    result = spaces_left
    return result

print(solution())