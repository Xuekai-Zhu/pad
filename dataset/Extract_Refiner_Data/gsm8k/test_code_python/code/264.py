def solution():
    
    # Define the prices of newspaper and television ads
    NEWSPAPER_PRICE = 5
    TVENO_PRICE = 75

    # Define the number of newspaper and television ads purchased
    newspaper_ads = 50
    television_ads = 15

    # Calculate the total cost of the newspaper ads
    newspaper_cost = newspaper_ads * NEWSPAPER_PRICE

    # Calculate the total cost of the television ads
    tven_cost = television_ads * TVENO_PRICE

    # Calculate the total cost of all the ads
    total_cost = newspaper_cost + tven_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())