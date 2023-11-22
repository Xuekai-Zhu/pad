def solution():
    
    # Define the original prices of the T-shirts and the shoes
    tshirt_price = 8
    shoe_price = 40

    # Calculate the discounted prices of the T-shirts
    tshirt_discounted_price = tshirt_price * 0.5

    # Calculate the discounted price of the shoes
    shoe_discounted_price = shoe_price * 0.6

    # Calculate the total cost of the T-shirts and the shoes
    total_cost = (tshirt_discounted_price * 2) + shoe_discounted_price

    # return the result
    result = total_cost
    return result

print(solution())