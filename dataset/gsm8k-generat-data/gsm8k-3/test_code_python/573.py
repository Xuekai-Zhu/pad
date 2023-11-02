def solution():
    """Bert was able to sell 8 toy phones for $18 each, while Tory was able to sell 7 toy guns for $20 each. How much more did Bert earn than Tory?"""
    # Define the price of each toy
    PHONE_PRICE = 18
    GUN_PRICE = 20

    # Define the number of toys sold by each person
    bert_sold = 8
    tory_sold = 7

    # Calculate the earnings of each person
    bert_earnings = bert_sold * PHONE_PRICE
    tory_earnings = tory_sold * GUN_PRICE

    # Calculate the difference in earnings
    earnings_diff = bert_earnings - tory_earnings

    # Display the difference in earnings
    result = earnings_diff
    return result

print(solution())