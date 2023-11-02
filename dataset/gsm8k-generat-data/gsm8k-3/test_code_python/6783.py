def solution():
    """Lyle wants to buy himself and his friends a sandwich and a pack of juice. A sandwich costs $0.30 while a pack of juice costs $0.2. If Lyle has $2.50, how many of his friends can have a sandwich and a pack of juice?"""
    # Define the price of a sandwich and a pack of juice
    SANDWICH_PRICE = 0.30
    JUICE_PRICE = 0.20

    # Define the amount of money Lyle has
    lyle_money = 2.50

    # Calculate the maximum number of sandwiches Lyle can buy
    max_sandwiches = int(lyle_money // SANDWICH_PRICE)

    # Calculate the maximum number of juices Lyle can buy
    max_juices = int(lyle_money // JUICE_PRICE)

    # Calculate the maximum number of friends who can have a sandwich and a pack of juice
    max_friends = min(max_sandwiches, max_juices) - 1 # subtract 1 for Lyle himself

    # Display the maximum number of friends who can have a sandwich and a pack of juice
    result = max_friends
    return result

print(solution())