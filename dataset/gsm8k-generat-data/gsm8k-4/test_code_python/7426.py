def solution():
    """We harvested 405 kg of apples. 90 kg were used to make fruit juice and 60 kg was given to a restaurant. The rest were sold in 5 kg bags and their sale brought in $408. What was the selling price of one bag of apples?"""
    # Define the total amount of apples harvested
    total_apples = 405

    # Define the amount of apples used for juice and given to the restaurant
    apples_used = 90 + 60

    # Calculate the amount of apples sold in kg
    apples_sold = total_apples - apples_used

    # Convert the amount of apples sold to bags of 5 kg
    bags_sold = apples_sold / 5

    # Calculate the selling price of one bag of apples
    price_per_bag = 408 / bags_sold

    # Round the price to the nearest cent
    price_per_bag = round(price_per_bag, 2)

    # Return the result
    result = price_per_bag
    return result

print(solution())