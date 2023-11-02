def solution():
    """Michael ran a bakeshop and had to fill an order for 5 peach pies, 4 apple pies and 3 blueberry pies.  Each pie recipe called for 3 pounds of fruit each.  At the market, produce was on sale for $1.00 per pound for both blueberries and apples.  The peaches each cost $2.00 per pound.  How much will Michael spend at the market buying the fruit for his pie order?"""
    # Define the number of pies and the amount of fruit needed for each
    peach_pies = 5
    apple_pies = 4
    blueberry_pies = 3
    fruit_per_pie = 3

    # Define the prices of the different fruits
    peach_price = 2.00
    apple_price = 1.00
    blueberry_price = 1.00

    # Calculate the total amount of each fruit needed
    total_peaches = peach_pies * fruit_per_pie
    total_apples = apple_pies * fruit_per_pie
    total_blueberries = blueberry_pies * fruit_per_pie

    # Calculate the total cost of each fruit
    peach_cost = total_peaches * peach_price
    apple_cost = total_apples * apple_price
    blueberry_cost = total_blueberries * blueberry_price

    # Calculate the total cost of all fruits
    total_cost = peach_cost + apple_cost + blueberry_cost

    # return the result
    result = round(total_cost, 2)
    return result

print(solution())