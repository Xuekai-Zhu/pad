def solution():
    """Roman the Tavernmaster has $20 worth of gold coins. He sells 3 gold coins to Dorothy. After she pays him, he has $12. How many gold coins does Roman have left?"""
    # Define the initial amount of gold coins and their value
    initial_coins = 20
    coin_value = initial_coins / 20

    # Define the number of coins sold to Dorothy and calculate the new amount of gold coins
    sold_coins = 3
    remaining_value = 12 / coin_value
    remaining_coins = remaining_value

    # Display the number of coins Roman has left
    result = remaining_coins
    return result

print(solution())