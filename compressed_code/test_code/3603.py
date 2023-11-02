def solution():
    
    total_marbles = 50
    white_marbles = 20
    red_marbles = blue_marbles = (total_marbles - white_marbles) / 2
    removed_marbles = 2 * (white_marbles - blue_marbles)
    marbles_left = total_marbles - removed_marbles
    result = marbles_left
    return result

print(solution())