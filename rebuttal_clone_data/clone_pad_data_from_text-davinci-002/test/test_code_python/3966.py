def solution():
    red_marbles = 20
    blue_marbles = 30
    removed_red_marbles = 3
    removed_blue_marbles = removed_red_marbles * 4
    total_marbles_left = red_marbles - removed_red_marbles + blue_marbles - removed_blue_marbles
    result = total_marbles_left
    return result

print(solution())