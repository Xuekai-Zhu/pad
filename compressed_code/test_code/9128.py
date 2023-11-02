def solution():
    
    wolfgang_marbles = 16
    ludo_marbles = wolfgang_marbles + (1/4 * wolfgang_marbles)
    wl_marbles = wolfgang_marbles + ludo_marbles
    michael_marbles = (2/3) * wl_marbles
    total_marbles = wolfgang_marbles + ludo_marbles + michael_marbles
    equal_share = total_marbles // 3
    result = equal_share
    return result

print(solution())