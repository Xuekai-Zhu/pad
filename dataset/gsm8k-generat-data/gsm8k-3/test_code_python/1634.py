def solution():
    """Alexa has a lemonade stand where she sells lemonade for $2 for one cup.
    If she spent $20 on ingredients, how many cups of lemonade does she need to sell
    to make a profit of $80?"""
    # Define the cost and price per cup of lemonade
    COST_PER_CUP = 20 / 100  # $20 for ingredients to make 100 cups
    PRICE_PER_CUP = 2

    # Calculate the profit per cup of lemonade
    PROFIT_PER_CUP = PRICE_PER_CUP - COST_PER_CUP

    # Calculate the number of cups of lemonade to sell for a profit of $80
    cups_to_sell = int(80 / PROFIT_PER_CUP)

    # Display the number of cups to sell
    result = cups_to_sell
    return result

print(solution())