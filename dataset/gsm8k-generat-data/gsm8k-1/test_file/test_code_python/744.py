def solution():
    """Carl has four times as many marbles as Sean and Sean has half as many marbles as Cal. 
    If Sean has 56 marbles, how many marbles do Carl and Cal have combined?"""
    sean_marbles = 56
    cal_marbles = sean_marbles * 2
    carl_marbles = sean_marbles * 4
    total_marbles = cal_marbles + carl_marbles
    result = total_marbles
    return result

print(solution())