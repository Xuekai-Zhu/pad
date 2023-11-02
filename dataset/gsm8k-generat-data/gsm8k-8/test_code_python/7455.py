def solution():
    # Calculate the revenue from tire repairs
    tire_revenue = 300 * 20

    # Calculate the cost of tire repairs
    tire_cost = 300 * 5

    # Calculate the revenue from complex repairs
    complex_revenue = 2 * 300

    # Calculate the cost of complex repairs
    complex_cost = 2 * 50

    # Calculate the total revenue
    total_revenue = tire_revenue + complex_revenue + 2000

    # Calculate the total cost
    total_cost = tire_cost + complex_cost + 4000

    # Calculate the profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())