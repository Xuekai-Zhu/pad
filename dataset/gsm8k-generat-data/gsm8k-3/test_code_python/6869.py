def solution():
    """William and Harry played 15 rounds of tic-tac-toe. William won 5 more rounds than Harry. How many rounds did William win?"""
    # Let's assume Harry won x rounds
    x = (15 - 5) / 2
    
    # William won 5 more rounds than Harry
    william_rounds = x + 5

    # Display the number of rounds William won
    result = william_rounds
    return result

print(solution())