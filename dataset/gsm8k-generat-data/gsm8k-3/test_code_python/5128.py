def solution():
    """James pays $1000 for advertising.  It brought 100 customers to his site and 80% of those bought something at the store that cost $25.  How much profit does he gain from the ad?"""
    # Define the cost of advertising and the revenue per customer
    AD_COST = 1000
    REVENUE_PER_CUSTOMER = 25

    # Calculate the number of customers who made a purchase
    customer_count = 100
    purchase_rate = 0.8
    purchased_count = customer_count * purchase_rate

    # Calculate the total revenue from the purchases
    total_revenue = purchased_count * REVENUE_PER_CUSTOMER

    # Calculate the profit from the advertising
    profit = total_revenue - AD_COST

    # Display the profit
    result = profit
    return result

print(solution())