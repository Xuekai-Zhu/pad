def solution():
    """William and Harry played 15 rounds of tic-tac-to. William won 5 more rounds than Harry. How many rounds did William win?"""
    total_rounds = 15
    harry_won = (total_rounds - 5) / 2
    william_won = harry_won + 5
    result = william_won
    return result

print(solution())