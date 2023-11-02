def solution():
    """Beth had a set of 125 gold coins.  Carl gave Beth a gift of an additional 35 gold coins.  Then, Beth decided to sell half of her coins.  How many coins did Beth sell?"""
    # Beth's initial number of gold coins
    beth_coins = 125

    # The number of gold coins Carl gave Beth
    carl_gift = 35

    # Beth's new total number of gold coins
    total_coins = beth_coins + carl_gift

    # Beth's number of gold coins after selling half
    sold_coins = total_coins / 2

    # Display the number of coins sold
    result = sold_coins
    return result

print(solution())