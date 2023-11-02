def solution():
    # Calculate the price of the guitar with the deal and shipping from Guitar Center
    guitar_center_price = 1000 - (0.15 * 1000) + 100  
    # Calculate the price of the guitar with the deal and free shipping from Sweetwater
    sweetwater_price = 1000 - (0.1 * 1000)

    # Calculate the difference in price between the two stores
    price_difference = guitar_center_price - sweetwater_price
    result = price_difference
    return result

print(solution())