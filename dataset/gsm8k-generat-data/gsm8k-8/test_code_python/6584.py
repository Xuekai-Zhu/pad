def solution():
    # Define the prices of each item
    tshirt_price = 20
    pant_price = 80
    shoe_price = 150

    # Calculate the discounted prices of each item
    tshirt_discounted_price = tshirt_price * 0.9
    pant_discounted_price = pant_price * 0.9
    shoe_discounted_price = shoe_price * 0.9

    # Calculate the total cost before discount
    total_cost = 4 * tshirt_price + 3 * pant_price + 2 * shoe_price

    # Calculate the total cost after discount
    total_discounted_cost = 4 * tshirt_discounted_price + 3 * pant_discounted_price + 2 * shoe_discounted_price

    result = total_discounted_cost
    return result

print(solution())