def solution():
    """Henry wants to buy a t-shirt, a pair of jeans and a pair of socks. The jeans are twice the price of the t-shirt, and the t-shirt is $10 more expensive than the socks. The socks cost $5. How much does Henry need to pay for the pair of jeans?"""
    # Define the cost of the socks
    SOCKS_PRICE = 5

    # Calculate the cost of the t-shirt
    tshirt_price = SOCKS_PRICE + 10

    # Calculate the cost of the jeans
    jeans_price = tshirt_price * 2

    # Display the cost of the jeans
    result = jeans_price
    return result

print(solution())