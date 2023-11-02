def solution():
    # Define the percentage of profits received by company A and B
    a_percentage = 60/100
    b_percentage = 40/100

    # Calculate the total profit received by company B
    b_profit = 60000

    # Calculate the total combined profit before distribution
    total_profit = b_profit / b_percentage

    # Calculate the profit received by company A
    a_profit = total_profit * a_percentage
    result = a_profit
    return result

print(solution())