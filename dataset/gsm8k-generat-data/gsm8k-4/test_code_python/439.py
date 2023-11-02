def solution():
    """Timothy has $50 to spend at a souvenir shop. He sees some t-shirts that cost $8 each, key chains that sell 3 pieces for $2, and bags that cost $10 each. Timothy buys 2 t-shirts and 2 bags. How many pieces of key chains can he buy with the amount of money he has left?"""
    # Define the amount of money Timothy has to spend
    total_money = 50

    # Define the cost of each item
    tshirt_cost = 8
    keychain_cost = 2/3
    bag_cost = 10

    # Determine the cost of the items Timothy has bought
    tshirt_total = 2 * tshirt_cost
    bag_total = 2 * bag_cost
    items_total = tshirt_total + bag_total

    # Determine the amount of money left after buying the items
    money_left = total_money - items_total

    # Determine the number of keychains Timothy can buy with the money left
    keychain_count = int(money_left / keychain_cost)

    # Return the result
    result = keychain_count
    return result

print(solution())