def solution():
    """Tobias is a tractor salesman. His salary is based on the number of tractors he sells.  For every red tractor he sells, he gets paid 10% of the sales price for each tractor.  For every green tractor he sells, he gets paid 20% of the sales price for each tractor.  This week, he sold 2 red tractors and 3 green tractors.  The price of a single red tractor is $20,000.  This week, Tobias's salary was $7000.  What is the full price of a single green tractor, in dollars?"""
    # Define the price of a red tractor and the number of red tractors sold
    red_price = 20000
    red_tractors_sold = 2

    # Define Tobias' salary and the percentage of sales that come from green tractors
    salary = 7000
    green_percentage = 0.2

    # Calculate the total sales from green tractors
    green_sales = (salary - (red_tractors_sold * (red_price * 0.1))) / green_percentage

    # Calculate the price of a single green tractor
    green_price = green_sales / 3

    # Return the result
    result = green_price
    return result

print(solution())