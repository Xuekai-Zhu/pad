def solution():
    
    # Define the initial commission rate and the sales worth $1000
    commission_rate = 0.3
    sales_worth = 1000

    # Calculate the commission earned from selling goods worth $2500
    commission_earned = commission_rate * sales_worth

    # Calculate the commission earned from sales over $1000
    commission_over_1000 = commission_rate * sales_worth

    # Calculate the commission earned from sales over $1000
    commission_earned += commission_over_1000

    # Return the total commission earned
    result = commission_earned
    return result

print(solution())