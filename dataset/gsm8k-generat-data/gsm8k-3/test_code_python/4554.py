def solution():
    """Michael ran a bakeshop and had to fill an order for 5 peach pies, 4 apple pies and 3 blueberry pies.  Each pie recipe called for 3 pounds of fruit each.  At the market, produce was on sale for $1.00 per pound for both blueberries and apples.  The peaches each cost $2.00 per pound.  How much will Michael spend at the market buying the fruit for his pie order?"""
    # Define the cost per pound of each type of fruit
    APPLE_COST = 1
    BLUEBERRY_COST = 1
    PEACH_COST = 2

    # Define the number of pies to be made
    peach_pies = 5
    apple_pies = 4
    blueberry_pies = 3

    # Calculate the total pounds of fruit needed
    total_pounds = (peach_pies + apple_pies + blueberry_pies) * 3

    # Calculate the total cost of the fruit
    peach_cost = peach_pies * 3 * PEACH_COST
    apple_cost = apple_pies * 3 * APPLE_COST
    blueberry_cost = blueberry_pies * 3 * BLUEBERRY_COST
    total_cost = peach_cost + apple_cost + blueberry_cost

    # Display the total cost of the fruit
    result = total_cost
    return result

print(solution())