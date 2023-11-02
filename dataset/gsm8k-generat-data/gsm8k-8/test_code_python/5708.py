def solution():
    # Define variables
    reuben_price = x
    pastrami_price = x + 2

    # Calculate revenue from Reuben and pastrami sandwiches
    reuben_revenue = reuben_price * 10
    pastrami_revenue = pastrami_price * 5

    # Calculate total revenue
    total_revenue = reuben_revenue + pastrami_revenue

    # Set total revenue equal to $55 and solve for pastrami price
    pastrami_price = (55 - (10 * x)) / 5
    
    result = pastrami_price
    return result

print(solution())