def solution():
    """Martha needs 4 cups of berries and 2 cups of heavy cream to make 1 quart of ice cream. She wants to make 1 quart of strawberry ice cream and 1 quart of raspberry ice cream. At the farmers market, the 2 cup packages of strawberries are $3.00 each and the 2 cup package of raspberries are $5.00 each. The heavy cream is sold for $4.00 for a 4 cup container. How much will it cost her to make 1 quart of each ice cream?"""
    
    # Define the required quantities for making 1 quart of ice cream
    berries_per_quart = 4
    cream_per_quart = 2
    
    # Calculate the cost of strawberries needed for 1 quart of strawberry ice cream
    strawberry_cost = 3 * (berries_per_quart/2) 
    
    # Calculate the cost of raspberries needed for 1 quart of raspberry ice cream
    raspberry_cost = 5 * (berries_per_quart/2)
    
    # Calculate the cost of heavy cream needed for 2 quarts of ice cream
    cream_cost = 4
    
    # Calculate the total cost of ingredients for making 2 quarts of ice cream
    total_cost = (strawberry_cost + raspberry_cost + cream_cost) * 2
    
    result = total_cost
    return result

print(solution())