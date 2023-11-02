def solution():
    # Calculate the number of rounds William won
    total_rounds = 15
    harry_wins = (total_rounds - 5) / 2  # William won 5 more rounds than Harry, so Harry won (total_rounds - 5) rounds
    william_wins = harry_wins + 5  # William won 5 more rounds than Harry
    result = william_wins
    return result

print(solution())