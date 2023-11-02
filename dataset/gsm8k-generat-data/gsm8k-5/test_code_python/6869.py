def solution():
    total_rounds = 15  # William and Harry played 15 rounds of tic-tac-toe
    difference = 5  # William won 5 more rounds than Harry

    # Calculate the number of rounds William won
    william_wins = (total_rounds + difference) / 2

    result = william_wins
    return result

print(solution())