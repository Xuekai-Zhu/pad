def solution():
    """James buys 20 coins of a cryptocurrency at $15 each. The value of the coins increases by 2/3. He sells coins to recoup his original investment. How many coins did he sell?"""
    # Define the number of coins bought and the original price
    NUM_COINS_BOUGHT = 20
    ORIGINAL_PRICE = 15

    # Calculate the new price of the coins after the increase
    new_price = ORIGINAL_PRICE + (2/3 * ORIGINAL_PRICE)

    # Calculate the total value of the coins after the increase
    total_value = NUM_COINS_BOUGHT * new_price

    # Calculate the number of coins James needs to sell to recoup his original investment
    coins_to_sell = int(total_value / ORIGINAL_PRICE)

    # Display the number of coins James sold
    result = coins_to_sell
    return result

print(solution())