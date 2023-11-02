def solution():
    """Elsa and her sister watch an opera show every year at Central City Opera. Last year, opera seating cost $85 per ticket. This year, it costs $102. What is the percent increase in the cost of each ticket?"""
    # Define the ticket prices for last year and this year
    last_year_price = 85
    this_year_price = 102

    # Calculate the difference in price and divide by the original price
    increase_percent = ((this_year_price - last_year_price) / last_year_price) * 100

    # Display the percent increase
    result = increase_percent
    return result

print(solution())