def solution():
    """Susan is playing a board game with 48 spaces from the starting space to the winning end space of the game. On the first turn, she moves forward eight spaces. On the second turn, she moves two spaces, but lands on a space that sends her back five spaces. On the third turn, she moves forward six more spaces. How many spaces does she have to move to reach the ending space and win the game?"""
    current_space = 8
    current_space += 2
    current_space -= 5
    current_space += 6
    spaces_left_to_win = 48 - current_space
    result = spaces_left_to_win
    return result

print(solution())