def solution():
    """When Erick went to the market to sell his fruits, he realized that the price of lemons had risen by $4 for each lemon. 
    The price of grapes had also increased by half the price that the price of lemon increased by per grape. 
    If he had planned to sell the lemons at $8 and the grapes at $7, and he had 80 lemons and 140 grapes in his basket, 
    how much money did he collect from selling the fruits at the new prices?"""
    
    # Define the original prices of lemons and grapes
    LEMON_PRICE_ORIG = 8
    GRAPE_PRICE_ORIG = 7
    
    # Define the increase in price for lemons and grapes
    LEMON_INCREASE = 4
    GRAPE_INCREASE = LEMON_INCREASE / 2
    
    # Define the number of lemons and grapes in the basket
    num_lemons = 80
    num_grapes = 140
    
    # Calculate the new prices of lemons and grapes
    lemon_price_new = LEMON_PRICE_ORIG + LEMON_INCREASE
    grape_price_new = GRAPE_PRICE_ORIG + GRAPE_INCREASE
    
    # Calculate the total earnings from selling the fruits at the new prices
    total_earnings = (num_lemons * lemon_price_new) + (num_grapes * grape_price_new)
    
    # Display the total earnings
    result = total_earnings
    return result

print(solution())