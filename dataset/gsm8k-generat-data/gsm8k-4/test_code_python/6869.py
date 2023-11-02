def solution():
    """William and Harry played 15 rounds of tic-tac-toe. William won 5 more rounds than Harry. How many rounds did William win?"""
    # Define the number of rounds played and the difference in wins between William and Harry
    rounds_played = 15
    win_difference = 5

    # Calculate the number of rounds won by Harry
    harry_wins = (rounds_played - win_difference) / 2

    # Calculate the number of rounds won by William
    william_wins = harry_wins + win_difference

    result = william_wins
    return result

print(solution())