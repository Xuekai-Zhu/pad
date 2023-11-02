def solution():
    """Susan is playing a board game with 48 spaces from the starting space to the winning end space of the game. On the first turn, she moves forward eight spaces. On the second turn, she moves two spaces, but lands on a space that sends her back five spaces. On the third turn, she moves forward six more spaces. How many spaces does she have to move to reach the ending space and win the game?"""
    starting_space = 0
    winning_space = 48
    turn1_spaces = 8
    turn2_spaces_forward = 2
    turn2_spaces_backward = 5
    turn3_spaces = 6
    current_space = starting_space + turn1_spaces + turn2_spaces_forward - turn2_spaces_backward + turn3_spaces
    spaces_left = winning_space - current_space
    result = spaces_left
    return result

print(solution())