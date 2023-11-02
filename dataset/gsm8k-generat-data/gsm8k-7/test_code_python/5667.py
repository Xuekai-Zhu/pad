def solution():
    Leonard_wallet_price = 50
    Leonard_sneakers_price = 100
    Michael_backpack_price = 100
    Michael_jeans_price = 50

    # Calculate the total cost of Leonard's purchases
    Leonard_total_cost = Leonard_wallet_price + (2 * Leonard_sneakers_price)

    # Calculate the total cost of Michael's purchases
    Michael_total_cost = Michael_backpack_price + (2 * Michael_jeans_price)

    # Calculate the total cost of both purchases
    total_cost = Leonard_total_cost + Michael_total_cost
    result = total_cost
    return result

print(solution())