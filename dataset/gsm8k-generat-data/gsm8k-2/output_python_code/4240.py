def solution():
    """Three friends Wolfgang, Ludo, and Michael, went to Walmart and bought marbles. Wolfgang bought 16 marbles, Ludo bought 1/4 times more marbles than Wolfgang, and Michael bought 2/3 times as many marbles as the number of marbles both Wolfgang and Ludo bought. If they combined their marbles and decided to share them equally, how many marbles did each get?"""
    wolfgang_marbles = 16
    ludo_marbles = wolfgang_marbles * 1.25
    both_marbles = wolfgang_marbles + ludo_marbles
    michael_marbles = both_marbles * (2/3)
    total_marbles = wolfgang_marbles + ludo_marbles + michael_marbles
    each_gets = total_marbles / 3
    result = each_gets
    return result

print(solution())