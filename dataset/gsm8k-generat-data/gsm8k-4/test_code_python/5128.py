def solution():
    """James pays $1000 for advertising. It brought 100 customers to his site and 80% of those bought something at the store that cost $25. How much profit does he gain from the ad?"""
    # Define the cost of the advertising and the price of the product
    ad_cost = 1000
    product_price = 25

    # Calculate the number of customers who made a purchase
    purchasing_customers = 100 * 0.8

    # Calculate the total revenue from those purchases
    revenue = purchasing_customers * product_price

    # Calculate the profit after deducting the cost of the advertising
    profit = revenue - ad_cost

    result = profit
    return result

print(solution())