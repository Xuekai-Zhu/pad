def solution():
    """Noemi lost $400 on roulette and $500 on blackjack. How much money did Noemi begin with if she still had $800 in her purse?"""
    # Define the amount of money lost on roulette and blackjack
    roulette_loss = 400
    blackjack_loss = 500

    # Define the amount of money left in Noemi's purse
    remaining_money = 800

    # Calculate the total amount of money Noemi had initially
    initial_money = roulette_loss + blackjack_loss + remaining_money

    # return the result
    result = initial_money
    return result

print(solution())