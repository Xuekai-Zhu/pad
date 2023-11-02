def solution():
    """Marco owns an ice cream truck. His ice cream cones are $5 each. If his expenses are 80% of total sales for the day, how many ice cream cones would he need to sell to make a $200 profit for the day?"""
    # Define the price per ice cream cone
    ICE_CREAM_PRICE = 5

    # Define the target profit and the percentage of sales that goes towards expenses
    TARGET_PROFIT = 200
    EXPENSES_PERCENTAGE = 0.8

    # Calculate the total sales needed to achieve the target profit
    target_sales = (TARGET_PROFIT / (1-EXPENSES_PERCENTAGE))

    # Calculate the number of ice cream cones that need to be sold
    num_cones = target_sales / ICE_CREAM_PRICE

    # Round up to the nearest whole number
    num_cones = math.ceil(num_cones)

    # return the result
    result = num_cones
    return result

print(solution())