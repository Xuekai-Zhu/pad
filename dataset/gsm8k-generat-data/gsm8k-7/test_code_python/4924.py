def solution():
    starting_amount = 100
    winnings = 65
    losses = 50

    # Calculate the total amount won or lost
    net_amount = starting_amount + winnings - losses

    # Calculate the amount lost
    amount_lost = starting_amount - net_amount
    result = amount_lost
    return result

print(solution())