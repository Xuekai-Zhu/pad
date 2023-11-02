def solution():
    """Henry wants to buy a t-shirt, a pair of jeans and a pair of socks. The jeans are twice the price of the t-shirt, and the t-shirt is $10 more expensive than the socks. The socks cost $5. How much does Henry need to pay for the pair of jeans?"""
    socks_price = 5
    tshirt_price = socks_price + 10
    jeans_price = 2 * tshirt_price
    result = jeans_price
    return result

print(solution())