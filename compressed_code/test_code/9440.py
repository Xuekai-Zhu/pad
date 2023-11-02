def solution():
    
    total_marbles = 50
    white_marbles = 20
    red_marbles = blue_marbles = (total_marbles - white_marbles) / 2

    diff_white_blue = white_marbles - blue_marbles
    marbles_removed = 2 * diff_white_blue
    marbles_left = total_marbles - marbles_removed

    result = marbles_left
    return result

print(solution())