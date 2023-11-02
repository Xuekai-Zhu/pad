def solution():
    sock_cost = 5  # cost of socks
    tshirt_cost = sock_cost + 10  # cost of t-shirt is $10 more than that of socks
    jeans_cost = 2 * tshirt_cost  # cost of jeans is twice that of t-shirt

    # Calculate the total cost of t-shirt, jeans and socks
    total_cost = tshirt_cost + jeans_cost + sock_cost
    jeans_price = jeans_cost  # The price of jeans is the cost of jeans
    
    result = jeans_price
    return result

print(solution())