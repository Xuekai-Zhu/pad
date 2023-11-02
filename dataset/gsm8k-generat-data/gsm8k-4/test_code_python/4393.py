def solution():
    """Hallie is an artist. She wins an art contest, and she receives a $150 prize. She sells 3 of her paintings for $50 each. How much money does she make in total from her art?"""
    # Define the initial prize money and the price of each painting
    prize_money = 150
    painting_price = 50

    # Calculate the total amount of money earned from selling paintings
    painting_earnings = 3 * painting_price

    # Calculate the total amount of money earned from art
    total_earnings = prize_money + painting_earnings

    # return the result
    result = total_earnings
    return result

print(solution())