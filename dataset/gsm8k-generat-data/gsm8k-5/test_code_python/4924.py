def solution():
    # Initial amount Diane has
    initial_amount = 100

    # Amount won in 5 hands
    amount_won = 65

    # Total amount after winning the 5 hands
    total_amount = initial_amount + amount_won

    # Amount lost while betting bigger
    amount_lost = total_amount - 50

    # Total amount lost in all
    total_loss = amount_lost - initial_amount
    result = total_loss
    return result

print(solution())