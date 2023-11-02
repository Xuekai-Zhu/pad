def solution():
    sock_price = 5
    tshirt_price = sock_price + 10
    jeans_price = 2 * tshirt_price

    total_cost = jeans_price + tshirt_price + sock_price
    result = jeans_price
    return result

print(solution())