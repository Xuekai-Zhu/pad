def solution():
    total_marbles = 72
    colors = 3
    marbles_per_color = total_marbles / colors
    lost_red = 5
    lost_blue = 2 * lost_red
    lost_yellow = 3 * lost_red
    total_lost = lost_red + lost_blue + lost_yellow
    result = total_marbles - total_lost
    return result

print(solution())