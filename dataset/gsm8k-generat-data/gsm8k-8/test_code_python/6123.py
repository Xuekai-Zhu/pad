def solution():
    # Define the sales prices of the red and green tractors
    red_price = 20000
    green_price = x  # unknown

    # Calculate the total sales and commission for the red tractors
    red_sales = 2 * red_price
    red_commission = 0.1 * red_sales

    # Calculate the total sales and commission for the green tractors
    green_sales = 3 * green_price
    green_commission = 0.2 * green_sales

    # Calculate total salary for Tobias and solve for the price of a green tractor
    total_salary = red_commission + green_commission
    green_price = (7000 - red_commission) / (0.2 * 3)

    result = green_price
    return result

print(solution())