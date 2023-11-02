def solution():
    # Define the total budget and the price of each item purchased
    total_budget = 200
    shirt_price = 30
    pants_price = 46
    coat_price = 38
    socks_price = 11
    belt_price = 18

    # Calculate the total price of the purchased items
    total_price = shirt_price + pants_price + coat_price + socks_price + belt_price

    # Calculate the amount spent on the shoes
    shoe_price = total_budget - total_price - 16

    result = shoe_price
    return result

print(solution())