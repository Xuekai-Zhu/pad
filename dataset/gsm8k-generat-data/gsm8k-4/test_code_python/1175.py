def solution():
    """Henry wants to buy a t-shirt, a pair of jeans and a pair of socks. The jeans are twice the price of the t-shirt, and the t-shirt is $10 more expensive than the socks. The socks cost $5. How much does Henry need to pay for the pair of jeans?"""
    # Define the price of the socks
    socks_price = 5

    # Calculate the price of the t-shirt
    tshirt_price = socks_price + 10

    # Calculate the price of the jeans
    jeans_price = 2 * tshirt_price

    # Calculate the total price
    total_price = tshirt_price + jeans_price + socks_price

    # Return the price of the jeans
    result = jeans_price
    return result

print(solution())