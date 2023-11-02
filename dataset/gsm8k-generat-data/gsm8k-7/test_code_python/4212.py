def solution():
    initial_money = 400
    bet_multiplier = 2
    won_bet = True

    # Calculate the amount Braden would win if he won the bet
    if won_bet:
        winnings = initial_money * bet_multiplier
    else:
        winnings = 0

    # Calculate the total amount of money Braden would have
    total_money = initial_money + winnings
    result = total_money
    return result

print(solution())