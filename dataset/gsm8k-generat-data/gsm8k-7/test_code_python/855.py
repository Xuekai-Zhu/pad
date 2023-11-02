def solution():
    roulette_loss = 400
    blackjack_loss = 500
    remaining_money = 800

    # Calculate the total amount of money Noemi lost
    total_loss = roulette_loss + blackjack_loss

    # Calculate the initial amount of money Noemi had
    initial_money = total_loss + remaining_money
    result = initial_money
    return result

print(solution())