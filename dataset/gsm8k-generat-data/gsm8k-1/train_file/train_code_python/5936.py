def solution():
    """Beth has 72 marbles of three colors. Each color has the same amount of marbles. If Beth loses 5 red, twice as many blue, and three times as many yellow ones than red ones, how many marbles does she have left?"""
    total_marbles = 72
    colors = 3
    marbles_per_color = total_marbles // colors
    red_marbles = marbles_per_color
    blue_marbles = marbles_per_color
    yellow_marbles = marbles_per_color
    
    red_marbles -= 5
    blue_marbles -= 2 * 5
    yellow_marbles -= 3 * 5
    
    total_remaining_marbles = red_marbles + blue_marbles + yellow_marbles
    result = total_remaining_marbles
    
    return result

print(solution())