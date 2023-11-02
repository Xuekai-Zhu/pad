def solution():
    """Gloria has five times as many dimes as quarters in her graduation money. She decides to put 2/5 of the quarters aside for future use. If she has 350 dimes, calculate the combined number of quarters and dimes she has after putting aside 2/5 of the quarters?"""
    
    # Let's assume the number of quarters as x
    # Then the number of dimes will be 5x
    # Also, after putting aside 2/5 of the quarters, she will be left with 3/5 of the quarters, which is (3/5)x
    
    # Calculate the total amount of money before putting aside any quarters
    total_money = 0.25*x*x + 0.10*5*x*5*x

    # Calculate the total amount of money in the 2/5 of the quarters she put aside
    aside_money = 0.2*0.25*x*x

    # Calculate the total amount of money she has left
    remaining_money = total_money - aside_money

    # Calculate the total number of dimes she has
    total_dimes = 350

    # Calculate the total number of quarters she has left
    remaining_quarters = remaining_money/0.25

    # Calculate the combined number of quarters and dimes she has
    total_coins = remaining_quarters + total_dimes

    # Display the combined number of quarters and dimes she has
    result = total_coins
    return result

print(solution())