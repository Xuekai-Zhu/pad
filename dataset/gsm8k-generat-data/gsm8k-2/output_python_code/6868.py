def solution():
    """William and Harry played 15 rounds of tic-tac-toe. William won 5 more rounds than Harry. How many rounds did William win?"""
    total_rounds = 15
    difference = 5
    william_wins = (total_rounds + difference) / 2
    result = william_wins
    return result

print(solution())