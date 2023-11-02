def solution():
    """Timothy has $50 to spend at a souvenir shop. He sees some t-shirts that cost $8 each, key chains that sell 3 pieces for $2, and bags that cost $10 each. Timothy buys 2 t-shirts and 2 bags. How many pieces of key chains can he buy with the amount of money he has left?"""
    # Define the prices of each item
    TSHIRT_PRICE = 8
    KEYCHAIN_PRICE = 2 / 3
    BAG_PRICE = 10

    # Define the number of items Timothy buys
    tshirts = 2
    bags = 2

    # Calculate the total cost of the t-shirts and bags
    total_cost = (tshirts * TSHIRT_PRICE) + (bags * BAG_PRICE)

    # Calculate the amount of money Timothy has left
    money_left = 50 - total_cost

    # Calculate the maximum number of keychains Timothy can buy with the money left
    keychains = int(money_left / KEYCHAIN_PRICE)

    # Display the number of keychains Timothy can buy
    result = keychains
    return result

print(solution())