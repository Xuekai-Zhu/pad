def solution():
    """Elsa and her sister watch an opera show every year at Central City Opera. Last year, opera seating cost $85 per ticket. This year, it costs $102. What is the percent increase in the cost of each ticket?"""
    # Define the prices of last year and this year
    last_year_price = 85
    this_year_price = 102

    # Calculate the difference and the percent increase
    difference = this_year_price - last_year_price
    percent_increase = (difference / last_year_price) * 100

    # return the result
    result = percent_increase
    return result

print(solution())