def solution():
    # Define the number of rounds played
    total_rounds = 15

    # Calculate the number of rounds Harry won
    harry_won = (total_rounds - 5) / 2

    # Calculate the number of rounds William won
    william_won = harry_won + 5
    result = william_won
    return result

print(solution())