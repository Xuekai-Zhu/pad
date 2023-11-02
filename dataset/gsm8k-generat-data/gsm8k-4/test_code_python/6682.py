def solution():
    """Beth had a set of 125 gold coins. Carl gave Beth a gift of an additional 35 gold coins. Then, Beth decided to sell half of her coins. How many coins did Beth sell?"""
    # Define the initial number of gold coins
    initial_coins = 125

    # Add the gift from Carl
    total_coins = initial_coins + 35

    # Calculate the number of coins sold
    sold_coins = total_coins / 2

    # Return the result
    result = sold_coins
    return result

print(solution())