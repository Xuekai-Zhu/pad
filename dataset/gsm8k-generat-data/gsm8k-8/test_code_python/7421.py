def solution():
    # Calculate the amount the first winner will receive
    first_winner = 2400 / 3

    # Calculate the remaining amount of prize money after the first winner
    remaining_money = 2400 - first_winner

    # Calculate the amount each of the next ten winners will receive
    next_ten_winners = remaining_money / 10

    result = next_ten_winners
    return result

print(solution())