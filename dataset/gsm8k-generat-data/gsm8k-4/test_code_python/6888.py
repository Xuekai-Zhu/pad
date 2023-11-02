def solution():
    """A supermarket has pints of strawberries on sale. They sold 54 pints and made $216, which was $108 less than they would have made selling the same number of pints without the sale. How many more dollars does a pint of strawberries cost when not on sale?"""
    # Define the number of pints of strawberries sold and the total revenue from sales
    pints_sold = 54
    total_revenue = 216

    # Define the revenue per pint of strawberries
    revenue_per_pint = total_revenue / pints_sold

    # Define the revenue per pint of strawberries if there was no sale ($108 more than the actual revenue per pint)
    actual_revenue_per_pint = revenue_per_pint + 108/pints_sold

    # Calculate the difference in revenue per pint between the sale and no-sale prices
    price_difference = actual_revenue_per_pint - revenue_per_pint

    result = price_difference
    return result

print(solution())