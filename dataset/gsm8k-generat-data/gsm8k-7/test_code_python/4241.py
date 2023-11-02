def solution():
    wolfgang_marbles = 16
    ludo_marbles = wolfgang_marbles * (1 + 1/4)  # Ludo bought 1/4 times more than Wolfgang
    total_wolfgang_ludo_marbles = wolfgang_marbles + ludo_marbles
    michael_marbles = 2/3 * total_wolfgang_ludo_marbles  # Michael bought 2/3 times as many as both Wolfgang and Ludo together
    total_marbles = wolfgang_marbles + ludo_marbles + michael_marbles
    num_friends = 3
    each_gets = total_marbles / num_friends
    result = each_gets
    return result

print(solution())