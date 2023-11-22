def solution():
    
    # Define the cost and selling price of each bag of wheat
    COST_PER_BAG = 20
    PRICE_PER_BAG = 30

    # Define the cost and selling price of each bag of wheat
    COST_PER_BAG_TRANSPORT = 2
    PRICE_PER_BAG_SELLING = 400 / COST_PER_BAG_TRANSPORT

    # Calculate the number of bags sold
    bags_sold = (PRICE_PER_BAG_SELLING / COST_PER_BAG) * 4

    # Display the number of bags sold
    result = bags_sold
    return result

print(solution())