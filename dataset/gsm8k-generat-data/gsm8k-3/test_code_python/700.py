def solution():
    """Two white socks cost 25 cents more than a single brown sock. If two white socks cost 45 cents, how much would you pay for 15 brown socks?"""
    # Define the cost of two white socks and the price difference between a pair of white socks and a single brown sock
    WHITE_PAIR_PRICE = 45
    WHITE_BROWN_PRICE_DIFF = 25

    # Calculate the cost of a single white sock
    white_sock_price = WHITE_PAIR_PRICE / 2

    # Calculate the cost of a single brown sock
    brown_sock_price = white_sock_price - WHITE_BROWN_PRICE_DIFF

    # Calculate the total cost of 15 brown socks
    total_cost = 15 * brown_sock_price

    # Display the total cost of 15 brown socks
    result = total_cost
    return result

print(solution())