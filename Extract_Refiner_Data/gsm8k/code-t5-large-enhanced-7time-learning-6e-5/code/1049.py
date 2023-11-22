def solution():
    
    # Define the prices of the athletic gear
    top_price = 10
    shorts_price = top_price + 5
    shoes_price = 48 / 2
    socks_price = 8

    # Calculate the total cost of the athletic gear
    total_cost = top_price + shorts_price + shoes_price + socks_price

    # Subtract the coupon for the discounted price
    total_cost -= 2

    # return the result
    result = total_cost
    return result

print(solution())