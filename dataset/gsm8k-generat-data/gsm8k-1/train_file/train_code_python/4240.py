def solution():
    """Three friends Wolfgang, Ludo, and Michael, went to Walmart and bought marbles. Wolfgang bought 16 marbles, Ludo bought 1/4 times more marbles than Wolfgang, and Michael bought 2/3 times as many marbles as the number of marbles both Wolfgang and Ludo bought. If they combined their marbles and decided to share them equally, how many marbles did each get?"""
    wolfgang_marbles = 16
    ludo_marbles = wolfgang_marbles + (1/4 * wolfgang_marbles)
    wl_marbles = wolfgang_marbles + ludo_marbles
    michael_marbles = (2/3) * wl_marbles
    total_marbles = wolfgang_marbles + ludo_marbles + michael_marbles
    equal_share = total_marbles // 3
    result = equal_share
    return result

print(solution())