def solution():
    """Roman the Tavernmaster has $20 worth of gold coins. He sells 3 gold coins to Dorothy. After she pays him, he has $12. How many gold coins does Roman have left?"""
    # Define the value of each gold coin
    COIN_VALUE = 20 / 20  # Each coin is worth $1

    # Define the original number of gold coins Roman had
    original_coins = 20 / COIN_VALUE

    # Calculate the number of gold coins sold to Dorothy
    sold_coins = 3

    # Calculate the amount of money Roman received from Dorothy
    dorothy_paid = 12

    # Calculate the remaining amount of money Roman has
    remaining_money = 20 - dorothy_paid

    # Calculate the remaining number of gold coins Roman has
    remaining_coins = (original_coins - sold_coins) * remaining_money / 20

    # Display the remaining number of gold coins
    result = remaining_coins
    return result

print(solution())