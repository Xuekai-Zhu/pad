def solution():
    """Jen buys and sells candy bars. She buys candy bars for 80 cents each and sells them for a dollar each. If she buys 50 candy bars and sells 48 of them, how much profit does she make in cents?"""
    # Define the cost and selling price of each candy bar
    cost = 80
    selling_price = 100

    # Calculate the total cost of buying 50 candy bars
    total_cost = cost * 50

    # Calculate the total revenue from selling 48 candy bars
    total_revenue = selling_price * 48

    # Calculate the profit in cents
    profit = total_revenue - total_cost

    # return the result
    result = profit
    return result

print(solution())