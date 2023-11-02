def solution():
    starting_space = 0
    winning_space = 48

    # Calculate the spaces Susan moves on each turn
    turn1 = 8
    turn2 = 2 - 5  # She lands on a space that sends her back 5 spaces
    turn3 = 6

    # Calculate Susan's current space after 3 turns
    current_space = starting_space + turn1 + turn2 + turn3

    # Calculate the spaces Susan still needs to move to reach the winning space
    remaining_spaces = winning_space - current_space
    result = remaining_spaces
    return result

print(solution())