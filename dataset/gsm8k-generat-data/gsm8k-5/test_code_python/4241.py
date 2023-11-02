def solution():
    wolfgang_marbles = 16
    ludo_marbles = wolfgang_marbles * 1.25
    total_wolfgang_ludo_marbles = wolfgang_marbles + ludo_marbles
    michael_marbles = total_wolfgang_ludo_marbles * (2/3)

    total_marbles = wolfgang_marbles + ludo_marbles + michael_marbles
    share_each = total_marbles / 3
    result = share_each
    return result

print(solution())