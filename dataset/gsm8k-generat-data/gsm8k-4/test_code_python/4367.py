def solution():
    """Susan is playing a board game with 48 spaces from the starting space to the winning end space of the game. On the first turn, she moves forward eight spaces. On the second turn, she moves two spaces, but lands on a space that sends her back five spaces. On the third turn, she moves forward six more spaces. How many spaces does she have to move to reach the ending space and win the game?"""
    # Define the number of spaces Susan has moved so far
    total_spaces_moved = 0

    # On the first turn, she moves forward eight spaces
    total_spaces_moved += 8

    # On the second turn, she moves two spaces, but lands on a space that sends her back five spaces
    total_spaces_moved += 2 - 5

    # On the third turn, she moves forward six more spaces
    total_spaces_moved += 6

    # Calculate the number of spaces Susan has left to reach the ending space
    spaces_left = 48 - total_spaces_moved

    # Return the result
    result = spaces_left
    return result

print(solution())