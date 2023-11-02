def solution():
    cars_sold = 10  # James sold 10 cars that cost $25,000 each
    cars_price = 25000  # James sold 10 cars that cost $25,000 each
    cars_payment = 0.3 * cars_price  # The company paid 30% of the price to acquire the cars
    commission = 0.1  # James got a 10% commission on the profits

    # Calculate the total revenue from selling the cars
    total_revenue = cars_sold * cars_payment

    # Calculate the commission James received on the profits
    commission = total_revenue * commission

    # Calculate the profit James made
    profit = total_revenue - commission
    result = profit
    return result

print(solution())