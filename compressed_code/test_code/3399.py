def solution():
    
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