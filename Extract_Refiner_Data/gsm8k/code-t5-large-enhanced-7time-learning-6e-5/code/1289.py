def solution():
    
    # Define the number of bars produced in one day and the price per bar
    BARS_PER_DAY = 5000
    PRICE_PER_BAR = 2

    # Calculate the total number of bars produced in two weeks
    total_bars = BARS_PER_DAY * 7 * 2

    # Calculate the total revenue from selling all the bars
    total_revenue = total_bars * PRICE_PER_BAR

    # Display the total revenue
    result = total_revenue
    return result

print(solution())